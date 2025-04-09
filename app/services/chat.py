import os
from openai import OpenAI
from dotenv import load_dotenv
from app.core.info_imovel import informacoes_gerais

# Carrega variáveis do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Memória simples para manter o contexto da conversa
chat_history = []

def obter_resposta(pergunta):
    # Define o comportamento do assistente com base nas regras do imóvel
    instrucoes_sistema = (
        f"Você é um assistente imobiliário que responde de forma simpática e objetiva. "
        f"O imóvel fica no bairro {informacoes_gerais['bairro']}, próximo a {', '.join(informacoes_gerais['proximidades'])}. "
        f"Descrição do imóvel: {informacoes_gerais['descricao']}. "
        f"Nunca revele o nome do imóvel ou a rua. "
        f"Apenas mostre o valor após a simulação. "
        f"Use linguagem leve e clara."
    )

    # Prepara a mensagem completa que será enviada ao modelo
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

        # Atualiza a memória com pergunta e resposta
        chat_history.append({"role": "user", "content": pergunta})
        chat_history.append({"role": "assistant", "content": conteudo_resposta})

        return conteudo_resposta

    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

