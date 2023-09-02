from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# creating the class for the log in
class LoginForm(AuthenticationForm):
    fields = ('username', 'password')


# creating the class for the signup
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password1', 'password2')
