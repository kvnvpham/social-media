from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={
        'class': 'form-field',
        'placeholder': 'Enter First Name'
    }))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={
        'class': 'form-field',
        'placeholder': 'Enter Last Name'
    }))
    username = forms.CharField(label='Username', max_length=75, widget=forms.TextInput(attrs={
        'class': 'form-field',
        'placeholder': 'Enter Username'
    }))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-field',
        'placeholder': 'Enter Email'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-field',
        'placeholder': 'Enter Password'
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-field',
        'placeholder': 'Confirm Password'
    }))


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-field',
        'placeholder': 'Enter Username'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-field',
        'placeholder': 'Enter Password'
    }))