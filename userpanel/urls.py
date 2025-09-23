from django.urls import path
from . import views

app_name = 'userpanel'

urlpatterns = [
    path('', views.user_panel, name='user_panel'),
]