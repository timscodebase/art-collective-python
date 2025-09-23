from django import forms
from .models import Profile

class ThemeSelectForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['theme']
        widgets = {
            'theme': forms.Select(attrs={'onchange': 'this.form.submit()'}),
        }
        labels = {
            'theme': 'Select a Color Scheme',
        }