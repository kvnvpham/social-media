from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def home(request):
    return render(request, 'main/home.html')
