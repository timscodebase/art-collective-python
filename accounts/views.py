from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse # New import
from gallery.models import Image # Import the Image model
from .forms import ChangeUsernameForm, ProfileForm, ThemeForm # New import

@login_required
def user_panel_dashboard(request):
    """Enhanced dashboard with user statistics."""
    from gallery.models import Comment, Like
    
    # Get user statistics
    user_stats = {
        'image_count': Image.objects.filter(user=request.user).count(),
        'total_likes': Like.objects.filter(image__user=request.user).count(),
        'comments_count': Comment.objects.filter(user=request.user).count(),
    }
    
    return render(request, 'accounts/user_panel_dashboard.html', {
        'user_stats': user_stats
    })

@login_required
def manage_photos(request):
    user_images = Image.objects.filter(user=request.user).order_by('-id')
    paginator = Paginator(user_images, 6) # 6 images per page, same as gallery
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'accounts/manage_photos.html', {'page_obj': page_obj})

@login_required
def change_username(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'new_username': request.user.username})
            return redirect('accounts:dashboard') # Redirect to dashboard
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ChangeUsernameForm(instance=request.user) # Pre-populate with current username
    return render(request, 'accounts/change_username.html', {'form': form})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:dashboard')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/update_profile.html', {'form': form})

@login_required
def change_theme(request):
    if request.method == 'POST':
        print(f"Incoming POST data: {request.POST}") # DEBUG
        form = ThemeForm(request.POST, instance=request.user.profile)
        print(f"Form is valid: {form.is_valid()}") # DEBUG
        if not form.is_valid(): # DEBUG
            print(f"Form errors: {form.errors}") # DEBUG
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'new_theme': request.user.profile.theme})
            return redirect('accounts:dashboard')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ThemeForm(instance=request.user.profile)
    return render(request, 'accounts/change_theme.html', {'form': form})