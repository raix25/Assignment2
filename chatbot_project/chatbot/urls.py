from django.urls import path
from . import views

urlpatterns = [
   path('api/chat/', views.chat_api, name='chat_api'),
    path('clear/', views.clear_chat, name='clear_chat')
]