from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    class SignUpForm(UserCreationForm):
        fullname = forms.CharField(max_length=60, required=True, help_text='Optional')

        class Meta:
            model = User
            fields = [
                'username',
                'fullname',
                'password1',
                'password2',
            ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25, label="Enter username")
    password = forms.CharField(max_length=30, label='Password', widget=forms.PasswordInput)
