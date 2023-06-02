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
    following = profile.following.exclude(pk=request.user.id)
    followers = profile.followers.exclude(pk=request.user.id)

    return render(request, 'users/dashboard.html', {
        'profile': profile,
        'following': following,
        'followers': followers,
    })


@login_required
def view_profile(request, user_id):
    profile = get_object_or_404(UserProfile, user=user_id)
    following = profile.following.exclude(pk=user_id)
    followers = profile.followers.exclude(pk=user_id)

    current_user_follows = UserProfile.objects.filter(followers__id=request.user.id).exclude(pk=request.user.id)
    is_following = current_user_follows.filter(pk=str(user_id))

    return render(request, 'users/dashboard.html', {
        'profile': profile,
        'following': following,
        'followers': followers,
        'isFollowing': is_following,
    })


@login_required
def follow(request, profile_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    isFollowing = user_profile.following.filter(pk=str(profile_id))

    if not isFollowing:
        user_profile.following.add(profile_id)

    return redirect('main:home')


@login_required
def unfollow(request, profile_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    isFollowing = user_profile.following.filter(pk=str(profile_id))

    if isFollowing:
        user_profile.following.remove(profile_id)

    return redirect('main:home')