# art-collective-python/gallery/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ImageForm, CommentForm
from .models import Image, Comment

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)
            image_instance.user = request.user
            image_instance.save()
            # FIX: Redirect to the homepage after upload
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'gallery/upload_image.html', {'form': form})

def image_list(request):
    images = Image.objects.all().order_by('-id')
    return render(request, 'gallery/image_list.html', {'images': images})

@login_required
def user_image_list(request):
    images = Image.objects.filter(user=request.user).order_by('-id')
    return render(request, 'gallery/image_list.html', {'images': images, 'page_title': 'My Images'})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

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

    return render(request, 'gallery/image_detail.html', {
        'image': image,
        'comments': comments,
        'comment_form': comment_form
    })