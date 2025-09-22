from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import ImageForm, CommentForm
from .models import Image, Comment

def image_list(request):
    all_images = Image.objects.all().order_by('-id')
    paginator = Paginator(all_images, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery/image_list.html', {'page_obj': page_obj})

@login_required
def user_image_list(request, username):
    profile_user = get_object_or_404(User, username=username)
    images = Image.objects.filter(user=profile_user).order_by('-id')
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
            return redirect('gallery:image_detail', pk=image.pk)
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
        return redirect('gallery:user_image_list', username=request.user.username)
    return render(request, 'gallery/image_confirm_delete.html', {'image': image})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")
    if request.method == 'POST':
        image_pk = comment.image.pk
        comment.delete()
        return redirect('gallery:image_detail', pk=image_pk)
    # Redirect GET requests or show a confirmation page if desired
    return redirect('gallery:image_detail', pk=comment.image.pk)