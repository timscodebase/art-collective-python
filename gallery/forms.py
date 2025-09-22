# art-collective-python/gallery/forms.py

from django import forms
from .models import Image, Comment # Import Comment

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')

# Add this new form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write a comment...'}),
        }