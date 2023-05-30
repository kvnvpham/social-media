from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from post.forms import PostForm
from post.models import Post
from users.models import UserProfile


def index(request):
    return render(request, 'main/index.html')


@login_required
def home(request):
    if request.method == 'POST':
        submitted_form = PostForm(request.POST)

        if submitted_form.is_valid():
            post = submitted_form.save(commit=False)
            post.user = request.user
            post.save()
        
            return redirect('main:home')
    else:
        form = PostForm()
        following_posts = Post.objects.filter(user__profile__following__id=request.user.id).order_by('-posted_on')
        following_users = UserProfile.objects.filter(following__id=request.user.id)[:10]

    return render(request, 'main/home.html', {
        'form': form,
        'all_posts': following_posts,
        'following': following_users,
    })
