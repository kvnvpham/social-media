from django.db import models
from django.contrib.auth.models import User


class Chats(models.Model):
    users = models.ManyToManyField(User, related_name='user_chats', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified_on']
        verbose_name_plural = 'Chats'


class ChatMessages(models.Model):
    created_by = models.ForeignKey(User, related_name='message', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chats, related_name='chats', on_delete=models.CASCADE)
    content = models.TextField(max_length=150)

    class Meta:
        verbose_name_plural = 'Chat Messages'
    
    