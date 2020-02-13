from django.urls import path
from . import views
from django.conf import settings


app_name = "dash"
urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logoutView, name="logout"),
    path('projects', views.projectView, name='projects'),
    path('projects/<slug>', views.projectLessonView, name="project-slug"),
    path('<project>/<lesson>', views.workflow, name="project-lesson"),
    path('community', views.community, name='community')
]