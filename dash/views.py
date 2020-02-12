from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import Course, Lesson, LessonProgress, Quiz, QuizQuestion, QuizAnswer
from django.http import JsonResponse
from django.utils.safestring import mark_safe
import json

# Create your views here.
@login_required
def index(request):
    c = Course.objects.all()

    context = {'courses': c}
    return render(request, 'dash/index.html', context)

def courseView(request):
    context = {}
    return render(request, 'dash/index.html', context)

def projectLessonView(request, slug):
    c = Course.objects.get(s=slug)
    l = Lesson.objects.filter(course=c.id)

    # If LessonProgress does not exist, create it for current user logged in
    for lesson in l:
        try:
            p = LessonProgress.objects.get(user = request.user, lesson = lesson)
        except LessonProgress.DoesNotExist:
            cr = LessonProgress.objects.create(user=request.user, lesson=lesson)
            cr.save()

    # Calculate amount of lessons to show
    total_lessons = l.count()
    not_complete = LessonProgress.objects.filter(user=request.user, completed=0).count()-1
    complete = LessonProgress.objects.filter(user=request.user, completed=1).count()
    show_lessons = total_lessons-not_complete
    display_more = False

    print(complete-total_lessons)

    if complete - total_lessons == 0:
        display_more = False
    else:
        display_more = True

    lp = LessonProgress.objects.filter(user=request.user)[:show_lessons]

    context = {'projectTitle': c.title, 'lessons': l, 'lesson_progress': lp, 'display_more': display_more}
    return render(request, 'dash/lessons.html', context)

def projectView(request):
    p = Course.objects.all()
    context = {'project': p}
    return render(request, 'dash/projects.html', context)

def logoutView(request):
    logout(request)
    messages.add_message(request, messages.INFO, "You have been successfully logged out!")
    return redirect('front:index')

def checkAnswer(request):
    answer = request.GET.get('answer_id')
    q = QuizAnswer.objects.get(id=answer)
    nextLessonID = q.question.quiz.lesson.id+1
    nextLesson = Lesson.objects.get(id = nextLessonID)
    question = q.question
    maxEntries = QuizAnswer.objects.filter(question_id = question).count()

    data = {
        'correct': q.correct,
        'max': maxEntries,
        'next': nextLesson.title
    }

    return JsonResponse(data)

def workflow(request, project, lesson):
    print(lesson)
    l = Lesson.objects.get(s=lesson)
    print(l.id)
    q = QuizQuestion.objects.filter(quiz_id = l.id)
    qa = QuizAnswer.objects.all()

    if Lesson.objects.filter(id=l.id+1).exists():
        nextL = Lesson.objects.get(id=l.id+1)
    else:
        nextL = Lesson.objects.get(id=l.id)

    # generate room name
    course_slug = l.course.s
    lesson_slug = l.s
    combine_slug = course_slug + lesson_slug
    room_name = combine_slug.replace('-', '')

    context = {
        'lesson': l, 
        'questions': q, 
        'answers': qa, 
        'next':nextL, 
        'room_name': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    }
    return render(request, 'dash/workflow.html', context)

def updateLessonProgress(request):
    lesson = request.GET.get('lesson')

    try:
        l = LessonProgress.objects.get(user=request.user, lesson_id=lesson)
        l.completed = True
        l.save()

        data = {
            'success': True
        }
    except Exception as e:
        data = {
            'except': e
        }

    return JsonResponse(data)