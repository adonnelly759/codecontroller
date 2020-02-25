from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User


def user_exists(username):
    return User.objects.filter(username=username).exists()

class NewUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class' : 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        data = self.cleaned_data.get("email")

        if user_exists(data):
            raise forms.ValidationError("Email already exists. Try logging in!")

        return data

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ("email")

class ResetPassword(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class' : 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ("new_password1", "new_password2")