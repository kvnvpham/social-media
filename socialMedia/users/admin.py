from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import UserProfile


admin.site.unregister(Group)
admin.site.unregister(User)


class ProfileInLine(admin.StackedInline):
    model = UserProfile


class UserAdmin(admin.ModelAdmin):
    model = User
    ordering = ['username']
    fieldsets = [
        (
            None,
            {
                'fields': ['username', 'password']
            }
        ),
        (
            'Personal Info',
            {
                'fields': ['first_name', 'last_name', 'email']
            }
        ),
        (
            'Important Dates',
            {
                'fields': ['last_login', 'date_joined']
            }
        )
    ]
    inlines = [ProfileInLine]


admin.site.register(User, UserAdmin)
