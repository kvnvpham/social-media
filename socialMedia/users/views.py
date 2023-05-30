from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, LoginForm
from .models import UserProfile


def register(request):
    if request.user.is_authenticated:
        return redirect('main:home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            new_user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            if new_user is not None:
                login(request, new_user)
                return redirect('main:home')
        else:
            form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {
        'form': form,
    })


def login_user(request):
    if request.user.is_authenticated:
        return redirect('main:home')

    if request.method == 'POST':
        user = authenticate(
            request, 
            username=request.POST['username'], 
            password=request.POST['password']
            )
        if user is not None:
            login(request, user)
            return redirect('main:home')
        else:
            messages.error(request, 'There Was An Error Logging In. Please Try Again.')
            form = LoginForm()
            return render(request, 'users/login.html', {
                'form': form
            })
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {
            'form': form,
        })


@login_required
def dashboard(request):
    profile = get_object_or_404(UserProfile, user=request.user.id)

    return render(request, 'users/dashboard.html', {
        'profile': profile,
    })
