from django import forms
from .models import ChatRoom
from django.core.validators import RegexValidator

class ChatRoomForm(forms.ModelForm):
    name = forms.CharField(
        label="New room name",
        validators=[
            RegexValidator(
                regex=r'^[-a-zA-Z0-9_]+$',
                message='Room names can only contain letters, numbers, hyphens, and underscores.',
            ),
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter a new room name',
            'autocomplete': 'off',
        })
    )

    class Meta:
        model = ChatRoom
        fields = ['name']