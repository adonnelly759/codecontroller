from django.db import models
from dash.models import Lesson
from django.contrib.auth.models import User
import random

# Create your models here.
# Trophies table
class Trophies(models.Model):
    action = models.CharField(default="Completed", max_length=255)
    title = models.CharField(max_length=255)

    def create_trophy(action, title):
        if not Trophies.objects.filter(title=title).exists():
            Trophies.objects.create(
                action= action,
                title = title
            )

    def __str__(self):
        return "Trophy for %s" % self.title

# Award table
class Award(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trophy = models.ForeignKey(Trophies, on_delete=models.CASCADE)
    awarded = models.DateTimeField(auto_now_add=True)
    colour = models.CharField(default="red", max_length=20)

    def award_user(user, trophy):
        rand = random.randint(1,5)

        if rand == 1:
            colour = "red"

        if rand == 2:
            colour = "blue"

        if rand == 3:
            colour = "gray"

        if rand == 4:
            colour = "yellow"

        if rand == 5:
            colour = "green"

        Award.objects.create(user=user, trophy=trophy, colour=colour)

    def __str__(self):
        return "Trophy for %s for %s" % (self.user.username, self.trophy.title)