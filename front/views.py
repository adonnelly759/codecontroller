# Imports from Django 
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Imports from app
from .forms import NewUserForm, ResetForm
from cc.settings import EMAIL_HOST_USER


# Create your views here.
def index(request):
    if request.method == 'POST':
        # User new user form
        form = NewUserForm(request.POST)
        # Form valid
        if form.is_valid():
            # Save form
            user = form.save()
            messages.success(request, 'Your account was successfully registered!')
            return redirect(reverse('front:login'))
    else:
        form = NewUserForm()
    return render(request, 'front/index.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        uname = request.POST.get('cc-email')
        pwd = request.POST.get('cc-password')
        # Authenticate user using Django authentication function
        user = authenticate(username=uname, password=pwd)
        # Check user exists
        if user is not None:
            # Log in user
            login(request, user)
            return redirect('dash:index')
        else:
            messages.error(request,'Username / Password was incorrect!')
            return redirect('front:login')           

    return render(request, 'front/login.html', {})

# Sign up
def signup(request):
    if request.method == 'POST':
        # New User Form
        form = NewUserForm(request.POST)
        # If form is valid       
        if form.is_valid():
            # save form 
            user = form.save()
            messages.success(request, 'Your account was successfully registered!')
            return redirect(reverse('front:login'))
    else:
        form = NewUserForm()
    return render(request, 'front/register.html', {'form': form})
