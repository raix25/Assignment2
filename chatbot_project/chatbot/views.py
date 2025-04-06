from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.conf import settings

# Initialize chatbot
chatbot = ChatBot(**settings.CHATTERBOT)

# Train the chatbot (optional)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")  # Basic training data

@csrf_exempt  # Disable CSRF for simplicity (enable in production)
def chat_api(request):
    if request.method == 'POST':
        user_input = request.POST.get('message', '').strip()
        if user_input:
            response = chatbot.get_response(user_input)
            return JsonResponse({'response': str(response)})
        return JsonResponse({'error': 'Empty message'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def clear_chat(request):
    if request.method == 'POST':
        chatbot.storage.drop()  # Clear all chat history
        return JsonResponse({'status': 'Chat cleared'})
    return JsonResponse({'error': 'Invalid request'}, status=400)
