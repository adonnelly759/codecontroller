from django.db import models
from django.utils.text import Truncator, slugify
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
import uuid

# Course table
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    s = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def short(self):
        return Truncator(self.description).chars(50)

    def save(self, *args, **kwargs):
        self.s = slugify(self.title)
        return super(Course, self).save(*args, **kwargs)

# Lesson table
class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True, config_name="special")
    shortDesc = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    s = models.SlugField(unique=True)    

    def __str__(self):
        return "%s - %s" % (self.title, self.course.title)

    def short(self):
        return Truncator(self.shortDesc).chars(50)

    def save(self, *args, **kwargs):
        self.s = slugify(self.title)
        super(Lesson, self).save(*args, **kwargs)

# Instructions table
class Instructions(models.Model):
    title = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - (%s / %s)" % (self.title, self.lesson.title, self.lesson.course.title)

    class Meta:
        verbose_name_plural = "Lesson Instructions"

# Lesson Progress table
class LessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    start = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    finish = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.user.get_full_name(), self.lesson.title)

    def percent(self):
        total = LessonProgress.objects.filter(lesson__course=self.lesson.course, user=self.user).count()
        done = LessonProgress.objects.filter(lesson__course=self.lesson.course, user=self.user, completed=True).count()
        return (done/total)*100

    class Meta:
        verbose_name_plural = "Lesson Progression"

# Quiz table
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quizes"

# Quiz Questions table
class QuizQuestion(models.Model):
    title = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.quiz.title, self.title)

    class Meta:
        verbose_name_plural = "Quiz Questions"

# Quiz Answers table
class QuizAnswer(models.Model):
    title = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s - %s" % (self.question.quiz.title, self.question.title, self.title)

    class Meta:
        verbose_name_plural = "Question Answers"