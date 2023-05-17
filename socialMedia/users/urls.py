from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm


app_name = 'users'
urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=LoginForm), name='login'),
    path('register/', views.register, name='register'),
]