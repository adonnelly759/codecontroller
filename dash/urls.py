from django.urls import path
from . import views
from django.conf import settings


app_name = "dash"
urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logoutView, name="logout"),
    path('course/<slug>', views.lessonView, name="lesson"),
]