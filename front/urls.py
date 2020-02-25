from django.urls import path, include
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from .forms import ResetForm, ResetPassword

app_name = "front"
urlpatterns = [
    path('', views.index, name='index'),
    path('pricing', views.plans, name='plans'),
    path('lessons', views.lessons, name="lessons"),
    path('accounts/login/', views.loginView, name="login"),
    path('accounts/signup', views.signup, name="signup"), 
    path('accounts/reset/', auth_views.PasswordResetView.as_view(form_class=ResetForm, success_url="done", template_name='front/forgot.html', email_template_name = 'front/reset_password_email.html'), name="password_reset"),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('front:password_reset_complete'), form_class=ResetPassword, template_name='front/forgot-reset.html'), name="password_reset_confirm"),
    path('accounts/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='front/forgot-complete.html'), name="password_reset_complete")  ,
    path('accounts/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='front/forgot-done.html'), name="password_reset_done"),
]