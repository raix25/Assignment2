from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'MyBot',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Hello',
            'output_text': 'Hi there!'
        },
        'chatterbot.logic.MathematicalEvaluation'
    ],
    read_only=True
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Add after initial training
additional_training = [
    "What is your name?",
    "My name is DjangoBot.",
    "What can you do?",
    "I can chat with you and answer questions.",
    "Who created you?",
    "I was created by a Django developer."
]

trainer = ListTrainer(chatbot)
trainer.train(additional_training)