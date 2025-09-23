from django import forms
from django.contrib.auth import get_user_model
from .models import Profile # New import

class ChangeUsernameForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['theme']
        widgets = {
            'theme': forms.RadioSelect # Use radio buttons for theme selection
        }
