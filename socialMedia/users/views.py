from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            new_user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            if new_user:
                login(request, new_user)
                return redirect('main:home')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {
        'form': form,
    })
