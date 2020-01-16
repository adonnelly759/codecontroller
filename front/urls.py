from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "front"
urlpatterns = [
    path('', views.index, name='index'),
    path('pricing', views.plans, name='plans'),
    path('lessons', views.lessons, name="lessons"),
    path('accounts/login/', views.loginView, name="login"),
    path('forgot', views.forgot, name="forgot"),
    path('accounts/signup', views.signup, name="signup"),
    path('accounts/reset/done', auth_views.PasswordResetCompleteView.as_view(template_name="front/reset_done.html"), name="password_reset_done"),
    path('accounts/reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="front/reset_confirm.html"), name="reset_confirm"),
    path('accounts/reset', auth_views.PasswordResetView.as_view(), name="password_reset"),
]