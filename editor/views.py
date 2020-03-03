from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dash.models import Course, Lesson, Instructions

# Create your views here.
@login_required
def index(request):
    return render(request, 'editor/index.html', {})