from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from badges.models import Award
from activity.models import Stream
from dash.models import LessonProgress
from chat.models import Message


# Signal for earning new badge
@receiver(post_save, sender=Award)
def new_badge(sender, instance, created, **kwargs):
    if created:
        Stream.new(
            actor=instance.user,
            verb="earned a badge for completing",
            title=instance.trophy.title,
            link="dash:badges"
        )

# Signal for completing lesson
@receiver(post_save, sender=LessonProgress)
def lesson_complete(sender, instance, created, **kwards):
    if not created and instance.completed:
        Stream.new(
            actor=instance.user,
            verb="completed",
            title=instance.lesson.title,
            link="dash:project-lesson %s %s" % (instance.lesson.course.s, instance.lesson.s)
        )

# Signal for chatting
@receiver(post_save, sender=Message)
def chat_message(sender, instance, created, **kwards):
    if created:
        Stream.new(
            actor=instance.author,
            verb="chatted in",
            title=instance.room.name,
            link="#"
        )

# Signal for settings change#
@receiver(post_save, sender=User)
def user_update(sender, instance, created, **kwargs):
    Stream.new(
            actor=instance,
            verb="updated profile settings",
            title="in Account",
            link="#"
        )