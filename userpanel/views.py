from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ThemeSelectForm

@login_required
def user_panel(request):
    if request.method == 'POST':
        form = ThemeSelectForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('userpanel:user_panel')
    else:
        form = ThemeSelectForm(instance=request.user.profile)
        
    return render(request, 'userpanel/panel.html', {'form': form})