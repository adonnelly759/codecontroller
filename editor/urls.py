from django.urls import path
from . import views

app_name = "editor"
urlpatterns = [
    path('/<course>/<slug>', views.index, name='index'),
]