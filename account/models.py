from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator, slugify
from datetime import datetime

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    streak = models.IntegerField(default=0)
    s = models.SlugField(unique=True)

    def __str__(self):
        return "Account for %s" % (self.user.first_name)

    def compareTime(self):
        if(self.user.last_login < datetime.now()):
            self.strak = self.streak+1

    def save(self, *args, **kwargs):
        self.s = slugify("%s %s" % (self.user.first_name, self.user.last_name))
        return super(Account, self).save(*args, **kwargs)