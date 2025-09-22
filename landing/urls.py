from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'landing'

urlpatterns = [
    path('', views.landing_page, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing:home'), name='logout'),
]