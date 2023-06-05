from django.contrib import admin

from .models import Chats, ChatMessages


class MessagesInline(admin.StackedInline):
    model = ChatMessages
    ordering = ['-created_at']
    extra = 0


class ChatsInline(admin.ModelAdmin):
    model = Chats
    inlines = [MessagesInline]


admin.site.register(Chats, ChatsInline)
