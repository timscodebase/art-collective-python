# art-collective-python/gallery/urls.py

from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('my-images/', views.user_image_list, name='user_image_list'),
    # Add this line for the detail page
    path('image/<int:pk>/', views.image_detail, name='image_detail'),
]