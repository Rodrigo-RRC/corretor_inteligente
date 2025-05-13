import os
from dotenv import load_dotenv
from openai import OpenAI
from app.core.info_imovel import informacoes_gerais
from app.core.info_mcmv import info_mcmv

# Carrega variáveis do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Memória simples para manter o histórico de conversa
chat_history = []

def obter_resposta(pergunta):
    instrucoes_sistema = """
Você é Bruna, uma agente virtual inteligente especializada em imóveis do programa Minha Casa Minha Vida. Seu papel é coletar apenas as informações necessárias para uma simulação de financiamento, sem parecer robô, sendo cordial, objetiva e adaptável conforme o contexto da conversa.

REGRAS DE CONDUTA:
- Nunca entregue o endereço do imóvel (mencione apenas 'próximo ao Bairro Geisel').
- Faça uma pergunta por vez e apenas quando necessário.
- Mantenha a conversa fluida, como uma atendente humana treinada faria.
- Após a coleta completa dos dados, os resultados da simulação serão enviados por você mesma (Bruna), sem repassar o atendimento ao corretor ainda.
- O corretor parceiro (Rodrigo) só assume o atendimento após a visita ser confirmada por SMS.

ABERTURA DA CONVERSA:
Olá! Sou a Bruna, sua corretora virtual — uma agente inteligente aqui pra te ajudar com imóveis do Minha Casa Minha Vida.

Este imóvel fica próximo ao Bairro Geisel, tem 1 suíte + 1 quarto, área de lazer completa, e está saindo a partir de R$ 178 mil.

Posso te ajudar de duas formas:

1️⃣ Ver se o imóvel combina com seu perfil  
2️⃣ Agendar uma visita (preciso antes fazer uma pré-análise)

Responda com 1 ou 2, por favor 😊

"""

    # Força a abertura da conversa na primeira interação
    if len(chat_history) == 0:
        pergunta = "Inicie a conversa"

    # Monta o contexto da conversa
    mensagens = [{"role": "system", "content": instrucoes_sistema}]
    mensagens.extend(chat_history)
    mensagens.append({"role": "user", "content": pergunta})

    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=mensagens,
            temperature=0.7
        )

        conteudo = resposta.choices[0].message.content.strip()

        # Atualiza o histórico
        chat_history.append({"role": "user", "content": pergunta})
        chat_history.append({"role": "assistant", "content": conteudo})

        return conteudo

    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

