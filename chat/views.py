from django.utils.safestring import mark_safe
from django.shortcuts import render
import json

# Render default index page
def index(request):
    return render(request, 'chat/index.html', {})

# Render chat room
def room(request, room_name):
    return render(request, 'chat/room.html', {
        # Pass json dumps for chat room
        'room_name': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username))
    })