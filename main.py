from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openai/gpt-3.5-turbo"

class Pergunta(BaseModel):
    mensagem: str

@app.post("/perguntar")
def perguntar(pergunta: Pergunta):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/Rodrigo-RRC",  # personalize
        "X-Title": "Corretor Inteligente",
    }

    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Você é um corretor inteligente e simpático, que responde com empatia, clareza e foco em imóveis populares."},
            {"role": "user", "content": pergunta.mensagem}
        ]
    }

    response = requests.post(OPENROUTER_URL, headers=headers, json=body)
    resposta = response.json()
    
    if "choices" in resposta:
        return {"resposta": resposta["choices"][0]["message"]["content"]}
    else:
        return {"erro": "Erro na resposta da IA", "detalhes": resposta}
