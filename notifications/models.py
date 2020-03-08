from django.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize

# Notification table
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    sent = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.user.first_name

    def new(user, content):
        Notification.objects.create(
            user = user,
            content = content
        )

    def get_date(self):
        return humanize.naturaltime(self.sent)