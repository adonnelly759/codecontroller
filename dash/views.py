# Django imports
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Import from app models and python
from .models import Course, Lesson, LessonProgress, Quiz, QuizQuestion, QuizAnswer
from badges.models import Trophies, Award
from .forms import EditProfileForm, EditPasswordForm
from activity.models import Stream
from notifications.models import Notification
import json

@login_required # Login decorator from Django
def index(request):
    # Get all courses
    c = Course.objects.all()

    # Pass courses object
    context = {'courses': c}
    return render(request, 'dash/index.html', context)

@login_required # Login decorator from Django
def courseView(request):
    context = {}
    return render(request, 'dash/index.html', context)

@login_required # Login decorator from Django
def editor(request):
    # Return python editor page
    return render(request, 'dash/editor.html', {})

@login_required # Login decorator from Django
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

    if complete - total_lessons == 0:
        # Set display_more flag to false
        display_more = False
    else:
        # Set flag to true
        display_more = True

    # Filter lesson progress model and show only limited number
    lp = LessonProgress.objects.filter(user=request.user)[:show_lessons]

    context = {'projectTitle': c.title, 'lessons': l, 'lesson_progress': lp, 'display_more': display_more}
    return render(request, 'dash/lessons.html', context)

@login_required # Login decorator from Django
def projectView(request):
    # Return all courses for project
    p = Course.objects.all()
    context = {'project': p}
    return render(request, 'dash/projects.html', context)

@login_required # Login decorator from Django
def logoutView(request):
    logout(request) # Use django logout function
    messages.add_message(request, messages.INFO, "You have been successfully logged out!")
    return redirect('front:index')

@login_required # Login decorator from Django
def checkAnswer(request):
    # Get answer id from ajax request
    answer = request.GET.get('answer_id')
    # Get quiz from answer id
    q = QuizAnswer.objects.get(id=answer)
    nextLessonID = q.question.quiz.lesson.id+1
    nextLesson = Lesson.objects.get(id = nextLessonID)
    question = q.question
    maxEntries = QuizQuestion.objects.filter(quiz_id=q.question.quiz.id).count()

    # Return data from the fileted queryset
    data = {
        'correct': q.correct,
        'max': maxEntries,
        'next': nextLesson.title
    }

    # Return as json object
    return JsonResponse(data)

@login_required # Login decorator from Django
def awardBadge(request):
    slug = request.GET.get('slug')
    action = request.GET.get('action')
    success = False

    # Elimitate user errors with try/except
    try:
        # Try to query the course model
        itemTitle = Course.objects.get(s=slug).title
    except:
        # If that fails query lesson model
        itemTitle = Lesson.objects.get(s=slug).title

    # Check if trophy exists, then award user or create it
    try:
        Trophies.objects.filter(title=slug).exists()
        t = Trophies.objects.get(title=slug)
        a = Award.award_user(request.user, t)
        success = True
    except:
        t = Trophies.create_trophy(action=action, title=itemTitle)
        new_t = Trophies.objects.get(title=itemTitle)
        a = Award.award_user(request.user, new_t)
        success = True


    data = {
        'success': success
    }

    return JsonResponse(data)

@login_required # Login decorator from Django
def workflow(request, project, lesson):
    l = Lesson.objects.get(s=lesson)
    q = QuizQuestion.objects.filter(quiz__lesson_id = l.id)
    qa = QuizAnswer.objects.all()

    # Check if a next lesson exists
    if Lesson.objects.filter(id=l.id+1).exists():
        nextL = Lesson.objects.get(id=l.id+1)
    else:
        nextL = Lesson.objects.get(id=l.id)

    # generate room name
    course_slug = l.course.s
    lesson_slug = l.s
    combine_slug = course_slug + lesson_slug
    room_name = combine_slug.replace('-', '')

    # Pass queryset to loop in template
    context = {
        'lesson': l, 
        'questions': q, 
        'answers': qa, 
        'next':nextL, 
        'room_name': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    }
    return render(request, 'dash/workflow.html', context)

@login_required # Login decorator from Django
def updateLessonProgress(request):
    # Get lesson id
    lesson = request.GET.get('lesson')

    # Try/except for lesson progress to update it
    try:
        l = LessonProgress.objects.get(user=request.user, lesson_id=lesson)
        l.completed = True
        l.save()

        # Pass success true for ajax response
        data = {
            'success': True
        }
    except Exception as e:
        data = {
            'except': e
        }

    return JsonResponse(data)

@login_required # Login decorator from Django
def community(request):
    # Community page, pass roomname and username
    # Check that it is safe and dump json
    context = {
        'room_name': mark_safe(json.dumps("community")),
        'username': mark_safe(json.dumps(request.user.username)),
    }
    return render(request, 'dash/community.html', context)

@login_required # Login decorator from Django
def trophy(request):
    # Filter awards by user
    a = Award.objects.order_by('-awarded').filter(user=request.user)

    # Use Django Paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(a, 3)

    try:
        a = paginator.page(page)
    except PageNotAnInteger:
        a = paginator.page(1)
    except EmptyPage:
        a = paginator.page(paginator.num_pages)

    context = {
        'award': a
    }

    return render(request, 'dash/trophy.html', context)

# Render activity view
@login_required # Login decorator from Django
def activity(request):
    s = Stream.objects.order_by('-when').filter(actor=request.user)

    # Use Django Paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(s, 10)

    try:
        s = paginator.page(page)
    except PageNotAnInteger:
        s = paginator.page(1)
    except EmptyPage:
        s = paginator.page(paginator.num_pages)

    return render(request, 'dash/activity.html', {'stream': s})

# Render notification view
@login_required # Login decorator from Django
def notifications(request):
    # Filter notifcation object
    n = Notification.objects.order_by('-sent').filter(user=request.user)

    # Use Django Paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(n, 5)

    try:
        n = paginator.page(page)
    except PageNotAnInteger:
        n = paginator.page(1)
    except EmptyPage:
        n = paginator.page(paginator.num_pages)

    return render(request, 'dash/notifications.html', {'notifications': n})

# Ajax notification to update
@login_required # Login decorator from Django
def notificationSeen(request):
    # Pass user object to user variable
    user = request.user

    # Update notifcation when seen
    try:
        notifications = Notification.objects.filter(seen=False, user=user)
        for n in notifications:
            n.seen = True
            n.save()
    except Exception:
        print("Failed")

    data = {
        'correct': True
    }

    return JsonResponse(data)

@login_required # Login decorator from Django
def getNotifications(request):
    user = request.user
    result = []
    # Get notifications per user
    try:
        n = Notification.objects.order_by('sent').filter(seen=False, user=user)
    except Exception:
        print("Failed")

    # Create json object for filtering in template
    for notifications in n:
        result.append({
            'content': notifications.content,
            'when': notifications.get_date()
        })

    data = {
        'correct': True,
        'notify': result,
        'count': n.count()
    }

    return JsonResponse(data)

# Leaderboards
@login_required # Login decorator from Django
def leaderboards(request):
    l = Award.objects.values('user', 'user__first_name', 'user__last_name').order_by('-total').annotate(total=Count('id'))

    # Use Django Paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(l, 10)

    try:
        l = paginator.page(page)
    except PageNotAnInteger:
        l = paginator.page(1)
    except EmptyPage:
        l = paginator.page(paginator.num_pages)

    return render(request, 'dash/leaderboards.html', {'leaderboards': l})

@login_required # Login decorator from Django
def settings(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        # Check if form is valid
        if form.is_valid():
            form.save()
            messages.info(request, "Updated profile successfully!")
            return redirect('/dash/settings')
        else:
            messages.error(request, "Failed to update profile!")
            return redirect('/dash/settings')
    else:
        form = EditProfileForm(instance=request.user)
        context = {
            'form': form
        }
    return render(request, 'dash/settings.html', context)

@login_required # Login decorator from Django
def password_settings(request):
    # Form posted
    if request.method == 'POST':
        form = EditPasswordForm(request.user, request.POST)
        # Check if form is valid
        if form.is_valid():
            # Save form
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse('dash:password-change'))
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        form = EditPasswordForm(request.user)
    return render(request, 'dash/password-change.html', {
        'form': form
    })