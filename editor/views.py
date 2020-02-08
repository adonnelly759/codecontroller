from django.shortcuts import render
from dash.models import Course, Lesson, Instructions

# Create your views here.
def index(request):
    return render(request, 'editor/index.html', {})