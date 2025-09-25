from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import models
from gallery.models import Image


def landing_page(request):
    """Enhanced landing page with recent images and better UX."""
    
    # Get recent popular images for the landing page
    recent_images = Image.objects.select_related('user').annotate(
        like_count=models.Count('like', distinct=True)
    ).order_by('-like_count', '-id')[:6]
    
    return render(request, 'landing/landing.html', {
        'recent_images': recent_images
    })


def signup(request):
    """User registration with enhanced feedback."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, 
                f'Welcome to Artist Collective, {user.username}! You can now login and start sharing your art.'
            )
            return redirect('login')
        else:
            messages.error(
                request,
                'Please correct the errors below to complete your registration.'
            )
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})