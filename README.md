# Bot FURIA CS 🇧🇷 🐾💥

Um chatbot interativo criado com Python e Telegram Bot API para fãs do time de CS da FURIA.

## 🧠 Funcionalidades

- Inicia conversa com menu interativo usando botões.
- Usuário pode interagir com o bot de forma natural, sem usar comandos prefixados com "/".
- Integração com IA via DeepSeek (OpenRouter API) para responder perguntas sobre o time.
- Respostas curtas e objetivas com base no contexto da FURIA.
- Ambiente seguro com variáveis de ambiente para dados sensíveis.

## 📸 Protótipo funcional

[Link Protótipo Funcional](https://biancabezerra.github.io/furia-chat-prototipo/)

## 🎥 Demonstração em vídeo

<p align="center">
<img src="Animação.gif" alt="Video de demonstração" />
</p>

## 🧪 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/biancaBezerra/furia-bot.git
cd seu-repositorio
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto e adicione:

```env
BOT_TOKEN=seu_token_aqui
API_KEY=seu_token_deepseek_aqui
```

### 5. Execute o bot

```bash
python bot.py
```

## 📁 Estrutura do projeto

```
├── ai.py                # Função que consulta a IA DeepSeek
├── main.py              # Arquivo principal com handlers do Telegram
├── requirements.txt     # Dependências do projeto
├── .env                 # Variáveis de ambiente (não versionado)
├── .gitignore           # Ignora venv, .env, __pycache__, etc.
```

## ✅ Requisitos

- Python 3.10+
- Conta no Telegram + Token do BotFather
- Chave de API do OpenRouter com acesso ao modelo DeepSeek


---

Feito com 💥 para a torcida FURIA.