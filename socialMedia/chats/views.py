from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Chats


@login_required
def chat_dashboard(request):
    value, results = '', []
    all_chats = Chats.objects.filter(users__in=[request.user.id])

    if request.method == 'POST':
        user = request.POST['search']
        value = user
        results = User.objects.filter(username__icontains=user)

    return render(request, 'chats/chats.html', {
        'all_chats': all_chats,
        'value': value,
        'results': results,
    })