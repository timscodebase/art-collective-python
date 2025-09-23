from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('galleries/', views.gallery_list, name='gallery_list'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('upload/', views.upload_image, name='upload_image'),
    path('image/<int:pk>/', views.image_detail, name='image_detail'),
    path('image/<int:pk>/delete/', views.delete_image, name='delete_image'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('like/<int:pk>/', views.like_image, name='like_image'),
]