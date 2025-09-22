from django import forms
from .models import ChatRoom

class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter a new room name',
                'aria-label': 'New room name',
                'autocomplete': 'off',
            })
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Add any custom validation here if needed, e.g., for reserved names.
        if ' ' in name:
            raise forms.ValidationError("Room names cannot contain spaces.")
        return name
