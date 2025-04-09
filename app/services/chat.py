import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Adicionando memória simples
chat_history = []

def obter_resposta(pergunta):
    chat_history.append({"role": "user", "content": pergunta})

    try:
        resposta = client.chat.completions.create(
            model="gpt-4",
            messages=chat_history,
            temperature=0.7
        )

        conteudo_resposta = resposta.choices[0].message.content.strip()
        chat_history.append({"role": "assistant", "content": conteudo_resposta})
        return conteudo_resposta

    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

