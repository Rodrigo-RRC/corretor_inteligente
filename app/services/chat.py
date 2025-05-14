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
    Você é Bruna, uma agente virtual inteligente especializada em imóveis do programa Minha Casa Minha Vida.
    Seu papel é conduzir o atendimento de forma empática e inteligente, entendendo o contexto da conversa e guiando o cliente com naturalidade até a simulação ou agendamento da visita.

    REGRAS DE CONDUTA:
    - Nunca entregue o endereço do imóvel (diga apenas "próximo ao Bairro Geisel").
    - Envie três fotos do imóvel após a apresentação textual, simulando pausas como se estivesse digitando.
    - Apresente as opções de entrada:
      1) É a primeira vez que tento comprar meu imóvel próprio
      2) Já tentei outras vezes, mas não consegui
      3) Já tenho carta aprovada e quero visitar o imóvel
    - Se a opção for 3, solicite a carta de crédito ou simulação via WhatsApp.
    - Se a opção for 1 ou 2, inicie uma coleta de informações para simulação.

   SEGUIMENTO DA COLETA:
   1. Quem vai financiar o imóvel com você? (Só você, com cônjuge, ou mais alguém?)
   2. Como é a forma de trabalho da(s) pessoa(s) que irá/irão financiar? (Carteira assinada, autônomo, MEI...)
   3. Qual é a renda familiar mensal total comprovada?
   4. Vocês têm ao menos 3 anos de carteira assinada (mesmo que somando diferentes empregos)?
   5. Qual a data de nascimento da pessoa que nasceu primeiro entre vocês?
   6. Vocês têm filhos ou outras pessoas que dependem financeiramente de vocês?
   7. Têm algum valor disponível para dar de entrada? (Pode usar FGTS)
"""

    if estado == "apresentacao":
        atualizar_estado(lead_id, "coletando_dados")
        return """Olá! Sou a Bruna, sua corretora virtual — uma agente inteligente aqui pra te ajudar com imóveis do Minha Casa Minha Vida.

   Este imóvel fica próximo ao Bairro Geisel, tem 1 suíte + 1 quarto, área de lazer completa, e está saindo a partir de R$ 178 mil.

   (Foto 1)
     ...aguarda...
   (Foto 2)
     ...aguarda...
   (Foto 3)

   Agora me diga:
   1️⃣ É a primeira vez que tenta comprar seu imóvel?
   2️⃣ Já tentou outras vezes e não conseguiu?
   3️⃣ Já tem carta aprovada e quer visitar o imóvel?

   Responda com 1, 2 ou 3, por favor 😊"""

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

        # GATILHOS que disparam pausa
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

