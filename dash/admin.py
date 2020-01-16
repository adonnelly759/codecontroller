from django.contrib import admin
from .models import Course, Lesson, LessonProgress, Instructions

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    prepopulated_fields = {'s': ('title',)} # new

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(LessonProgress)
admin.site.register(Instructions)
