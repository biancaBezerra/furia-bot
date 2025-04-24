import os
from dotenv import load_dotenv
import requests


load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

def ask_ai(pergunta):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [{"role": "user", "content": pergunta}]
    }

    response = requests.post(API_URL, json=data, headers=headers)

    if response.status_code == 200:
        resposta = response.json()['choices'][0]['message']['content']
        return resposta
    else:
        return f"Erro ao consultar a IA. Código: {response.status_code}"