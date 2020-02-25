from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import NewUserForm, ResetForm
from cc.settings import EMAIL_HOST_USER


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account was successfully registered!')
            return redirect(reverse('front:login'))
    else:
        form = NewUserForm()
    return render(request, 'front/index.html', {'form': form})

def plans(request):
    return render(request, 'front/plans.html', {})

def lessons(request):
    return render(request, 'front/lessons.html', {})

def loginView(request):
    if request.method == 'POST':
        uname = request.POST.get('cc-email')
        pwd = request.POST.get('cc-password')
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('dash:index')
        else:
            messages.error(request,'Username / Password was incorrect!')
            return redirect('front:login')           

    return render(request, 'front/login.html', {})

def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account was successfully registered!')
            return redirect(reverse('front:login'))
    else:
        form = NewUserForm()
    return render(request, 'front/register.html', {'form': form})
