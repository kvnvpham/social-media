from django.db import models
from django.contrib.auth.models import User


class Chats(models.Model):
    users = models.ManyToManyField(User, related_name='user_chats', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified_on']
        verbose_name_plural = 'Chats'

    def __str__(self):
        return str(self.created_at)


class ChatMessages(models.Model):
    created_by = models.ForeignKey(User, related_name='message', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chats, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField(max_length=150)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Chat Messages'

    def __str__(self):
        return f'{self.created_by}, {str(self.created_at)}'
    
    