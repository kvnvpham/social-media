from django.urls import path

from . import views


app_name = 'chats'
urlpatterns = [
    path('', views.chat_dashboard, name='chat_dashboard'),
    path('user/<int:chat_id>/', views.view_chat, name='chat'),
    path('start/<int:target_id>/', views.start_chat, name='start_chat'),
]