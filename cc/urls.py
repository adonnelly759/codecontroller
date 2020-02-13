"""cc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import dash.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dash/', include('dash.urls')),
    path('editor', include('editor.urls')),
    path('', include('front.urls')),
    path('ajax/check-answer', dash.views.checkAnswer, name="check-answer"),
    path('ajax/update-progress', dash.views.updateLessonProgress, name="update-progress"),
    path('ajax/award-badge', dash.views.awardBadge, name='award-badge'),
    path('chat/', include('chat.urls'))
]
