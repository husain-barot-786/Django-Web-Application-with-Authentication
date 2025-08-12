from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # This returns the validated user object
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
        else:
            # Add a generic invalid login error inside the form
            form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"login_form": form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"register_form": form})

@login_required
def profile(request):
    return render(request, "blog/profile.html")

@login_required
def user_logout(request):
    auth_logout(request)
    return redirect('login')
