from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse # New import
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Count # New import
from .forms import ImageForm, CommentForm
from .models import Image, Comment, Like # New import

def image_list(request):
    # Annotate images with like_count and check if current user liked it
    all_images = Image.objects.annotate(
        like_count=Count('like', distinct=True)
    ).order_by('-like_count', '-id') # Order by popularity, then by ID

    # Check if user is authenticated to determine if they liked an image
    if request.user.is_authenticated:
        liked_images = Like.objects.filter(user=request.user).values_list('image_id', flat=True)
        for image in all_images:
            image.user_has_liked = image.id in liked_images
    else:
        for image in all_images:
            image.user_has_liked = False # Not logged in, so no likes from this user

    paginator = Paginator(all_images, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery/image_list.html', {'page_obj': page_obj})

@login_required
def user_profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    images = Image.objects.filter(user=profile_user).annotate(
        like_count=Count('like', distinct=True)
    ).order_by('-like_count', '-id')

    if request.user.is_authenticated:
        liked_images = Like.objects.filter(user=request.user).values_list('image_id', flat=True)
        for image in images:
            image.user_has_liked = image.id in liked_images
    else:
        for image in images:
            image.user_has_liked = False

    paginator = Paginator(images, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery/user_profile.html', {'page_obj': page_obj, 'profile_user': profile_user})

def gallery_list(request):
    # Get the IDs of users who have at least one image
    user_ids_with_images = Image.objects.values_list('user_id', flat=True).distinct()
    # Get the User objects for those IDs
    artists = User.objects.filter(id__in=user_ids_with_images).order_by('username')
    return render(request, 'gallery/gallery_list.html', {'artists': artists})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)
            image_instance.user = request.user
            image_instance.save()
            return redirect('gallery:image_list')
    else:
        form = ImageForm()
    return render(request, 'gallery/upload_image.html', {'form': form})

@login_required
def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    comments = image.comments.all().order_by('-created_at')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.image = image
            new_comment.user = request.user
            new_comment.save()

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'username': new_comment.user.username,
                    'text': new_comment.text,
                    'created_at': new_comment.created_at.strftime("%b %d, %Y") # Format date for display
                })
            return redirect('gallery:image_detail', pk=image.pk)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': comment_form.errors})
    else:
        comment_form = CommentForm()
    return render(request, 'gallery/image_detail.html', {'image': image, 'comments': comments, 'comment_form': comment_form})

@login_required
def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if image.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this image.")
    if request.method == 'POST':
        image.delete()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'image_pk': pk})
        return redirect('gallery:user_profile', username=request.user.username)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'success': False, 'error': 'GET method not allowed for deletion.'}, status=405)
    return render(request, 'gallery/image_confirm_delete.html', {'image': image})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")
    if request.method == 'POST':
        image_pk = comment.image.pk
        comment.delete()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'comment_pk': pk})
        return redirect('gallery:image_detail', pk=image_pk)
    # Redirect GET requests or show a confirmation page if desired
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'success': False, 'error': 'GET method not allowed for deletion.'}, status=405)
    return redirect('gallery:image_detail', pk=comment.image.pk)

@login_required
def like_image(request, pk):
    if request.method == 'POST':
        image = get_object_or_404(Image, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, image=image)
        if not created:
            like.delete()

        # Get updated like count
        image.refresh_from_db() # Ensure image object has latest data
        new_like_count = image.like_set.count() # Use related_name for count

        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # Check if it's an AJAX request
            return JsonResponse({
                'like_count': new_like_count,
                'liked': created # True if a new like was created, False if unliked
            })
        # Fallback for non-AJAX requests
        return redirect(request.META.get('HTTP_REFERER', 'gallery:image_list'))
    return redirect('gallery:image_list')