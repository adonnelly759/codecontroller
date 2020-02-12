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
        return "%s said %s in room: %s" % (self.author.username, self.content, self.room.name)

    def last_10_messages(room_name):
        return Message.objects.filter(room__name=room_name)[:10]
