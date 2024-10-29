# Chatbot em Python

Um chatbot simples em Python desenvolvido com a biblioteca `nltk` para simular interações de texto e responder a perguntas comuns de forma personalizada. Este projeto é ideal para quem deseja explorar processamento de linguagem natural (NLP) e chatbots básicos.

## Funcionalidades (por enquanto)

- Responde a saudações como "Olá" e "Oi".
- Reconhece variações de frases, com ou sem acentuação.
- Processa perguntas sobre clima, hora e outras questões simples.
- Fácil de expandir para incluir novas perguntas e respostas.

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação principal.
- **NLTK (Natural Language Toolkit)**: Biblioteca para processamento de linguagem natural.

## Pré-requisitos

Antes de executar o chatbot, instale as dependências:

```bash
pip install nltk
```

Baixe o pacote `punkt`, necessário para a tokenização:

```python
import nltk
nltk.download('punkt')
```

## Como Usar

1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/seu-usuario/chatbot-python.git
   cd chatbot-python
   ```

2. Execute o chatbot:
   ```bash
   python chatbot.py
   ```

3. Interaja com o chatbot no terminal e teste perguntas como:
   - "Olá", "Oi", "Como está o clima?"
   - "Qual é a hora?", "Você pode me ajudar?"

## Estrutura do Projeto

- `chatbot.py`: Código principal do chatbot.
- `README.md`: Documentação do projeto.
- `LICENSE`: Licença do projeto (exemplo: MIT).

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e enviar pull requests com melhorias ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
```

Esse `README.md` cobre os principais pontos do projeto e orienta os usuários sobre como configurá-lo e usá-lo. Se você adicionar mais funcionalidades, é só atualizar o `README.md` com as novas informações.