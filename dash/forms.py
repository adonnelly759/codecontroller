from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

# Extension to style Django UserChangeForm
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control', 'aria-describedby': 'emailHelp'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = {
            'email',
            'first_name',
            'last_name'
        }

# Extentsion to style Django PasswordChangeForm
class EditPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password',  'class' : 'form-control', 'aria-describedby': 'emailHelp'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class' : 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class' : 'form-control'}))

    class Meta:
        model = User
        fields = {
            'old_password',
            'new_password1',
            'new_password2'
        }

