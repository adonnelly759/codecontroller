from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from badges.models import Award
from dash.models import Course
from account.models import Account
from .models import Notification

# Welome notification

# Earned badge
@receiver(post_save, sender=Award)
def notify_badge(sender, instance, created, **kwargs):
    if created:
        Notification.new(
            user = instance.user,
            content = "You earned a new bage!"
        )

# New Course
@receiver(post_save, sender=Course)
def notify_course(sender, instance, created, **kwargs):
    users = User.objects.all()
    if created:
        for user in users:
            Notification.new(
                user = user,
                content = "A new course has been added: %s!" % (instance.title)
        )

# New User created
@receiver(post_save, sender=Account)
def notify_user(sender, instance, created, **kwards):
    if created:
        Notification.new(
            user = instance.user,
            content = "Welcome to CodeController! We hope you learn a lot and can make use of your knew knowledge."
        )