from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ImageForm
from .models import Image

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:image_list')  # Redirect to the gallery page
    else:
        form = ImageForm()
    return render(request, 'gallery/upload_image.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'gallery/image_list.html', {'images': images})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
