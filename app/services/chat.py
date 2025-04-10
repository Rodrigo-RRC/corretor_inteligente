import os
from openai import OpenAI
from dotenv import load_dotenv
from app.core.info_imovel import informacoes_gerais

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Memória simples
chat_history = []

def obter_resposta(pergunta):
    texto = pergunta.lower()

    # 4. Filtros de resposta imediata para casos específicos
    if "nome sujo" in texto or "negativado" in texto:
        return "A Caixa não aprova com restrições. Primeiro é necessário regularizar o CPF. Posso te mostrar o caminho pra isso. 😊"

    if "subsídio" in texto or "ajuda do governo" in texto:
        return "Sim! O governo pode ajudar com subsídio. Vamos simular pra saber o quanto você pode receber."

    # 5. Instruções de estilo e comportamento do assistente
    instrucoes_sistema = (
        f"Você é um assistente imobiliário direto e simpático. "
        f"O imóvel está localizado no bairro {informacoes_gerais['bairro']}, próximo a {', '.join(informacoes_gerais['proximidades'])}. "
        f"Descrição do imóvel: {informacoes_gerais['descricao']}. "
        f"Nunca diga o nome do imóvel ou rua. Valor só após simulação. "
        f"Use linguagem leve e clara."
    )

    mensagens = [{"role": "system", "content": instrucoes_sistema}]
    mensagens.extend(chat_history)
    mensagens.append({"role": "user", "content": pergunta})

    try:
        resposta = client.chat.completions.create(
            model="gpt-4",
            messages=mensagens,
            temperature=0.7
        )

        conteudo_resposta = resposta.choices[0].message.content.strip()
        chat_history.append({"role": "user", "content": pergunta})
        chat_history.append({"role": "assistant", "content": conteudo_resposta})
        return conteudo_resposta

    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

