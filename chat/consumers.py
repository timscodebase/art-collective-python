import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("--- NEW WEBSOCKET CONNECTION ATTEMPT ---")
        try:
            print(f"Scope path: {self.scope.get('path')}")
            print(f"User: {self.scope.get('user')}")

            if not self.scope['user'].is_authenticated:
                print("Connection REJECTED: User not authenticated.")
                await self.close()
                return

            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f'chat_{self.room_name}'
            
            print(f"Attempting to add to Redis group: {self.room_group_name}")
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            print("Successfully added to group.")

            await self.accept()
            print("Connection ACCEPTED.")

        except Exception as e:
            print(f"!!! AN EXCEPTION OCCURRED IN connect METHOD: {e}")
            # Ensure connection is closed if an error occurs
            await self.close()


    async def disconnect(self, close_code):
        print(f"--- WEBSOCKET DISCONNECTED (Code: {close_code}) ---")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.scope['user'].username
        await self.channel_layer.group_send(
            self.room_group_name,
            {'type': 'chat_message', 'message': message, 'username': username}
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))