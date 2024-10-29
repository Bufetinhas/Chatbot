import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Pergunta o nome e o CPF do usuário para personalizar a conversa
def perguntar_nome_e_cpf():
    nome = input("Olá! Qual é o seu nome? ")
    cpf = input("Por favor, digite seu CPF (somente números): ")

    # Verifica se o CPF possui 11 dígitos
    while len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido! Digite novamente (somente números e com 11 dígitos).")
        cpf = input("Por favor, digite seu CPF (somente números): ")

    print(f"Prazer em conhecê-lo, {nome}!")
    return nome, cpf

# Função principal do chatbot
def chatbot():
    # Obtém o nome e o CPF do usuário
    nome_usuario, cpf_usuario = perguntar_nome_e_cpf()

    print(f"{nome_usuario}, como posso te ajudar hoje?")

    while True:
        # Recebe a entrada do usuário
        user_input = input(f"{nome_usuario}, você: ")

        # Tokeniza a entrada do usuário para uma análise mais simples
        tokens = word_tokenize(user_input.lower())

        # Saudações
        if any(word in tokens for word in ["olá", "oi", "ola"]):
            print(f"Chatbot: Olá, {nome_usuario}! Como posso ajudar você?")
        # Pergunta sobre clima
        elif any(word in tokens for word in ["clima", "tempo"]):
            print(f"Chatbot: {nome_usuario}, eu não posso te dar o clima atual, mas você pode verificar em um site de previsão do tempo!")
        # Pergunta sobre horário
        elif any(word in tokens for word in ["horas", "hora", "horário"]):
            print(f"Chatbot: Agora é só conferir no relógio, {nome_usuario}! O tempo está sempre passando.")
        # Encerrar a conversa
        elif any(word in tokens for word in ["sair", "tchau", "adeus"]):
            print(f"Chatbot: Tchau, {nome_usuario}! Foi bom conversar com você.")
            break
        # Pergunta sobre CPF
        elif any(word in tokens for word in ["cpf", "meu cpf"]):
            print(f"Chatbot: O CPF registrado é {cpf_usuario}.")
        # Resposta padrão para entradas não reconhecidas
        else:
            print(f"Chatbot: Desculpe, {nome_usuario}, eu ainda não sei responder isso.")

# Executa o chatbot
chatbot()
