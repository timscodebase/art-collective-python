# art-collective-python/gallery/admin.py

from django.contrib import admin
from .models import Image, Comment # Import Comment

admin.site.register(Image)
admin.site.register(Comment) # Register the new model