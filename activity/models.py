from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Stream(models.Model):
    actor = models.ForeignKey(User, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s %s" % (self.actor, self.verb, self.title)

    def new(actor, verb, title, link):
        Stream.objects.create(
            actor=actor,
            verb=verb,
            title=title,
            link=link
            )


