from django.shortcuts import render
from dash.models import Course, Lesson, Instructions

# Create your views here.
def index(request, course, slug):
    l = Lesson.objects.get(s=slug)
    cnt = Lesson.objects.filter(course=l.course)
    ins = Instructions.objects.filter(lesson=l)
    course = l.course.s

    current = 0
    prevSlug = ""
    prevDis = True
    nextEn = True

    for i in range(len(cnt)):
        if cnt[i].s == slug:
            current = i+1
            print(current)

    if current < cnt.count():
        nextSlug = cnt[current].s
    else:
        nextSlug = cnt[current-1].s
        nextEn = False

    if current-2 >= 0:
        prevSlug = cnt[current-2].s
    else:
        prevSlug = cnt[current].s
        prevDis = False
            
    context = {'lesson': l, 'course': course, 'cur': current, 'tot': cnt.count(), 'next': nextSlug, 'prev': prevSlug, 'prevDis': prevDis, 'nextEn': nextEn, 'ins': ins}
    return render(request, 'editor/index.html', context)