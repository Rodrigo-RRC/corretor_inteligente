import os
from dotenv import load_dotenv
from openai import OpenAI
from app.core.estado_lead import (
    inicializar_lead, atualizar_estado, obter_estado,
    adicionar_ao_historico, obter_historico
)

# Carrega variáveis do .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def obter_resposta(pergunta, lead_id):
    if obter_estado(lead_id) is None:
        inicializar_lead(lead_id)

    estado = obter_estado(lead_id)

    # PAUSA: aguardando comando de simulação
    if estado == "aguardando_simulacao" and not pergunta.startswith("#resposta_simulacao:"):
        return "Certo! Assim que a simulação estiver pronta, eu te aviso por aqui mesmo. 😉"

    # COMANDO INTERNO: resposta da simulação
    if pergunta.startswith("#resposta_simulacao:"):
        mensagem = pergunta.split(":", 2)[2]
        atualizar_estado(lead_id, "respondeu_simulacao")
        adicionar_ao_historico(lead_id, "assistant", mensagem)
        return mensagem

    # MONTA O PROMPT
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

    if estado == "apresentacao":
       atualizar_estado(lead_id, "coletando_dados")
       return """Olá! Sou a Bruna, sua corretora virtual — uma agente inteligente aqui pra te ajudar com imóveis do Minha Casa Minha Vida.

    Este imóvel fica próximo ao Bairro Geisel, tem 1 suíte + 1 quarto, área de lazer completa, e está saindo a partir de R$ 178 mil.

    Posso te ajudar de duas formas:

    1️⃣ Ver se o imóvel combina com seu perfil  
    2️⃣ Agendar uma visita (preciso antes fazer uma pré-análise)

    Responda com 1 ou 2, por favor 😊"""


    mensagens = [{"role": "system", "content": instrucoes_sistema}]
    mensagens.extend(obter_historico(lead_id))
    mensagens.append({"role": "user", "content": pergunta})

    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=mensagens,
            temperature=0.7
        )

        conteudo = resposta.choices[0].message.content.strip()

        adicionar_ao_historico(lead_id, "user", pergunta)
        adicionar_ao_historico(lead_id, "assistant", conteudo)

        # GATILHOS que disparam a pausa e mudam para aguardando_simulacao
        gatilhos_pausa = [
            "vou preparar uma simulação",
            "vou calcular os valores e condições",
            "em seguida te passo as informações",
            "posso prosseguir com a simulação",
            "vou calcular"
        ]

        if any(g in conteudo.lower() for g in gatilhos_pausa):
            atualizar_estado(lead_id, "aguardando_simulacao")
            return "Perfeito! Já coletei tudo que preciso.\nVou preparar a simulação com base nesses dados e te aviso por aqui mesmo assim que ela estiver pronta, tudo bem?"

        return conteudo

    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

