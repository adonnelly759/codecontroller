from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import Course, Lesson, LessonProgress

# Create your views here.
@login_required
def index(request):
    c = Course.objects.all()

    context = {'courses': c}
    return render(request, 'dash/index.html', context)

def courseView(request):
    context = {}
    return render(request, 'dash/index.html', context)

def lessonView(request, slug):
    c = Course.objects.get(s=slug)
    l = Lesson.objects.filter(course=c.id)

    # If LessonProgress does not exist, create it for current user
    for lesson in l:
        try:
            p = LessonProgress.objects.get(user = request.user, lesson = lesson)
            print(p.completed)
        except LessonProgress.DoesNotExist:
            #print("Does not exist")
            cr = LessonProgress.objects.create(user=request.user, lesson=lesson, code="")
            cr.save()

    context = {'contentTitle': c.title, 'lessons': l}
    return render(request, 'dash/lessons.html', context)


def logoutView(request):
    logout(request)
    messages.add_message(request, messages.INFO, "You have been successfully logged out!")
    return redirect('front:index')