from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', views.user_panel_dashboard, name='dashboard'),
    path('manage-photos/', views.manage_photos, name='manage_photos'),
    path('change-username/', views.change_username, name='change_username'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('change-theme/', views.change_theme, name='change_theme'),
]
