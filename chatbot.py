import random
import nltk
from nltk.chat.util import Chat, reflections
import re

# Baixar os dados necessários da biblioteca nltk 
nltk.download('punkt')

# Função para normalizar o texto do usuário, removendo acentos e pontuação
def normalize(text):
    text = text.lower()
    text = re.sub(r'[áàâã]', 'a', text)
    text = re.sub(r'[éèê]', 'e', text)
    text = re.sub(r'[íìî]', 'i', text)
    text = re.sub(r'[óòôõ]', 'o', text)
    text = re.sub(r'[úùû]', 'u', text)
    text = re.sub(r'[ç]', 'c', text)
    text = re.sub(r'[?!.,]', '', text)
    return text

# Defina padrões de entrada e saídas do chatbot
pairs = [
    [
        r"oi|olá|e ai|oi tudo bem|ola tudo bem|ola|eai|tudo bem",
        ["Olá! Como posso ajudar?", "Oi! Tudo bem?", "Oi, como você está?"]
    ],
    [
        r"qual seu nome|qual o seu nome|quem é você|como você se chama",
        ["Eu sou o seu chatbot amigo!", "Pode me chamar de Chatbot."]
    ],
    [
        r"como voce esta|como você está|tudo bem|como vai",
        ["Estou bem, obrigado! E você?", "Estou ótimo! Como você está?"]
    ],
    [
        r"o que voce pode fazer|o que você pode fazer|o que sabe fazer|como voce pode me ajudar",
        ["Posso conversar com você, responder perguntas e ajudar em algumas tarefas.", 
         "Eu sou um chatbot simples, mas estou aqui para ajudar."]
    ],
    [
        r"adeus|tchau|ate logo|ate mais",
        ["Tchau! Volte sempre que precisar.", "Até logo!"]
    ]
]

# Criação do chatbot usando o NLTK
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Chatbot: Olá! Eu sou seu chatbot. Digite 'sair' para encerrar a conversa.")
    while True:
        user_input = input("Você: ")
        normalized_input = normalize(user_input)  # Normaliza o texto do usuário
        if normalized_input == "sair":
            print("Chatbot: Até logo! Foi ótimo conversar com você.")
            break
        else:
            response = chatbot.respond(normalized_input)
            if response:
                print("Chatbot:", response)
            else:
                print("Chatbot: Desculpe, não entendi. Pode repetir?")

# Inicie o chatbot
start_chat()
