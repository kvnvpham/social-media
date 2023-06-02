from django.contrib import admin

from .models import Chats, ChatMessages


admin.site.register(Chats)
admin.site.register(ChatMessages)
