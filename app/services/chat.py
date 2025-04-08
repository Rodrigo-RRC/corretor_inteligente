import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def obter_resposta(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": pergunta}
            ]
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

