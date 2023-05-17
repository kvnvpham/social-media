from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-field',
        'placeholder': 'Enter Username'
    }))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-field',
        'placeholder': 'Enter Email'
    }))
    password1 = forms.CharField(label='Password', widget=forms.EmailInput(attrs={
        'class': 'form-field',
        'placeholder': 'Enter Password'
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.EmailInput(attrs={
        'class': 'form-field',
        'placeholder': 'Confirm Password'
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-field',
        'placeholder': 'Enter Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-field',
        'placeholder': 'Enter Password'
    }))