from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # this is the homepage route
    path('chat/', views.chat, name='chat'),
]