from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUser(UserCreationForm):
    email = forms.EmailField(required=False, help_text='Your email address')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
