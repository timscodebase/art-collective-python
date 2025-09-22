from django.shortcuts import render, redirect
from .models import ChatRoom
from .forms import ChatRoomForm
from django.contrib.auth.decorators import login_required

@login_required
def room_list(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            chat_room = form.save()
            return redirect('chat:chat_room', room_name=chat_room.name)
    else:
        form = ChatRoomForm()
    
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/room_list.html', {'rooms': rooms, 'form': form})

@login_required
def chat_room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})