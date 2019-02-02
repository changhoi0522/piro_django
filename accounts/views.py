# accounts/views.py
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) # default: '/account/login/'
    else:
        form = UserCreationForm()
    return render(request, './accounts/signup_form.html', {
        'form': form,
        })


def profile(request):
    return render(request, 'accounts/profile.html')
