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
    path('trophies', views.trophy, name='trophies'),
    path('community', views.community, name='community'),
    path('activity', views.activity, name="activity"),
    path('editor', views.editor, name="editor"),
    path('notifications', views.notifications, name='notifications'),
    path('leaderboards', views.leaderboards, name="leaderboards"),
    path('settings', views.settings, name='settings'),
    path('password', views.password_settings, name='password-change')
]