from django.shortcuts import render
from django.http import HttpResponse
from .chatterbot_instance import chatbot

def home(request):
    return HttpResponse("Hello! This is the chatbot view.")

def chat(request):
    return HttpResponse("My ChatBot Application Webpage")

from django.shortcuts import render
from django.utils.timezone import now

def home(request):
    return render(request, 'chatbot/chat.html', {'now': now()})


chat_history = []  # In-memory (use DB in production)

def chatbot_view(request):
    if request.method == "POST":
        user_msg = request.POST.get("message")
        bot_response = chatbot.get_response(user_msg)
        chat_history.append({"user": user_msg, "bot": str(bot_response)})
    return render(request, "chatbot/chat.html", {
        "chat_history": chat_history,
        "current_time": now().strftime("%H:%M:%S")
    })

def clear_chat(request):
    if request.method == "POST":
        chat_history.clear()
    return redirect("chat")

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import redirect

@login_required
def chat(request):
    return render(request, 'chatbot/chat.html', {'username': request.user.username})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            user, created = User.objects.get_or_create(username=username)
            login(request, user)
            return redirect('chat')
    return render(request, 'chatbot/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')