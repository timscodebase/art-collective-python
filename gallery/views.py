from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Count, Exists, OuterRef
from django.contrib import messages
from .forms import ImageForm, CommentForm
from .models import Image, Comment, Like

def image_list(request):
    all_images = Image.objects.all()

    if request.user.is_authenticated:
        user_likes = Like.objects.filter(
            image=OuterRef('pk'),
            user=request.user
        )
        all_images = all_images.annotate(user_has_liked=Exists(user_likes))
    else:
        for image in all_images:
            image.user_has_liked = False

    all_images = all_images.annotate(
        like_count=Count('like', distinct=True)
    ).order_by('-like_count', '-id')

    paginator = Paginator(all_images, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gallery/image_list.html', {'page_obj': page_obj})

def gallery_list(request):
    """Enhanced artists list with statistics."""
    user_ids_with_images = Image.objects.values_list('user_id', flat=True).distinct()
    artists = User.objects.filter(id__in=user_ids_with_images).select_related('profile').order_by('username')
    
    # Add statistics to each artist
    for artist in artists:
        artist.image_count = Image.objects.filter(user=artist).count()
        artist.total_likes = Like.objects.filter(image__user=artist).count()
        # Add bio from profile if it exists
        try:
            artist.bio = artist.profile.bio if hasattr(artist, 'profile') else None
        except:
            artist.bio = None
    
    return render(request, 'gallery/gallery_list.html', {'artists': artists})

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

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)
            image_instance.user = request.user
            image_instance.save()
            messages.success(request, f'🎨 "{image_instance.title}" has been uploaded successfully!')
            return redirect('gallery:image_list')
        else:
            messages.error(request, 'Please correct the errors below to upload your image.')
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
                    'created_at': new_comment.created_at.strftime("%b %d, %Y")
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

        image.refresh_from_db()
        new_like_count = image.like_set.count()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'like_count': new_like_count,
                'liked': created
            })
        return redirect(request.META.get('HTTP_REFERER', 'gallery:image_list'))
    return redirect('gallery:image_list')