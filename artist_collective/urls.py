from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from landing import views as landing_views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # App-specific URLs
    path('', include('landing.urls')),
    path('gallery/', include('gallery.urls')),
    # path('chat/', include('chat.urls')),
    # path('panel/', include('userpanel.urls')),
    
    # Centralized Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing:home'), name='logout'),
    path('signup/', landing_views.signup, name='signup'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_form.html',
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),
    path('chat/', include('chat.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)