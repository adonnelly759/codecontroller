from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'front/index.html', {})

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
    return render(request, 'front/register.html', {})

def forgot(request):
    return render(request, 'front/forgot.html', {})