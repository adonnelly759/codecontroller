from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Room(models.Model):
    name = models.CharField(max_length=255)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Message(models.Model):
    author = models.ForeignKey(User, related_name="author_messages", on_delete=models.CASCADE)
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages(roomName):
        return Message.objects.filter(room__name=roomName)[:10]
