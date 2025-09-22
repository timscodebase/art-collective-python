from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def landing_page(request):
    return render(request, 'landing/landing.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})