from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Chats
from .forms import MessageForm


@login_required
def chat_dashboard(request):
    value, results = '', []
    all_chats = Chats.objects.filter(users__in=[request.user.id])

    # Search Bar Function
    if request.method == 'POST':
        user = request.POST['search']
        value = user
        results = User.objects.filter(username__icontains=user)

    return render(request, 'chats/chats.html', {
        'all_chats': all_chats,
        'value': value,
        'results': results,
    })


@login_required
def view_chat(request, chat_id):
    chat = get_object_or_404(Chats, pk=chat_id)
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            chat_window = form.save(commit=False)
            chat_window.chat = chat
            chat_window.created_by = request.user
            chat_window.save()

            chat.save()

            return redirect('chats:chat', chat_id)

    return render(request, 'chats/chat_window.html', {
        'form': form,
        'chat': chat,
    })


@login_required
def start_chat(request, target_id):
    form = MessageForm()
    chat_exists = Chats.objects.filter(users__in=[request.user.id]).filter(users__in=[target_id])

    if chat_exists:
        chat = chat_exists.first()
        return render(request, 'chats/chat_window.html', {
            'form': form,
            'chat': chat,
        })
    
    new_chat = Chats.objects.create()
    new_chat.save()
    new_chat.users.add(request.user.id, target_id)
    new_chat.save()

    return render(request, 'chats/chat_window.html', {
        'form': form,
        'chat': new_chat,
    })