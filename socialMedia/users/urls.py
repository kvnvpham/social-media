from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm


app_name = 'users'
urlpatterns=[
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]