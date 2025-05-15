import os
from dotenv import load_dotenv
from openai import OpenAI
from app.core.estado_lead import (
    inicializar_lead, atualizar_estado, obter_estado,
    adicionar_ao_historico, obter_historico,
    obter_pergunta_atual, avancar_pergunta, perguntas_simulacao
)

# Carrega variáveis do .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def obter_resposta(pergunta, lead_id):
    if obter_estado(lead_id) is None:
        inicializar_lead(lead_id)

    estado = obter_estado(lead_id)

    if estado == "aguardando_simulacao" and not pergunta.startswith("#resposta_simulacao:"):
        return "Certo! Assim que a simulação estiver pronta, eu te aviso por aqui mesmo. 😉"

    if pergunta.startswith("#resposta_simulacao:"):
        mensagem = pergunta.split(":", 2)[2]
        atualizar_estado(lead_id, "respondeu_simulacao")
        adicionar_ao_historico(lead_id, "assistant", mensagem)
        return mensagem

    if estado == "apresentacao":
        atualizar_estado(lead_id, "coletando_dados")
        return (
            "Olá! Sou a Bruna, sua corretora virtual — uma agente inteligente aqui pra te ajudar com imóveis do Minha Casa Minha Vida.\n\n"
            "Este imóvel fica próximo ao Bairro Geisel, tem 1 suíte + 1 quarto, área de lazer completa, e está saindo a partir de R$ 178 mil.\n\n"
            "digitando...\n[Foto 1 - https://link-da-imagem.com/1.jpg]\n\ndigitando...\n[Foto 2 - https://link-da-imagem.com/2.jpg]\n\n"
            "digitando...\n[Foto 3 - https://link-da-imagem.com/3.jpg]\n\n"
            "Agora me diga:\n"
            "1️⃣ É a primeira vez que tenta comprar seu imóvel?\n"
            "2️⃣ Já tentou outras vezes e não conseguiu?\n"
            "3️⃣ Já tem carta aprovada e quer visitar o imóvel?\n\n"
            "Responda com 1, 2 ou 3, por favor 😊"
        )

    if estado == "coletando_dados" and pergunta.strip() in ["1", "2", "3"]:
        resposta = pergunta.strip()
        adicionar_ao_historico(lead_id, "user", resposta)

        if resposta == "1":
            return (
                "Perfeito! Para te ajudar da melhor forma, preciso fazer uma pequena simulação. Pode ser?"
            )
        elif resposta == "2":
            return (
                "Passado é passado. Agora é bola pra frente! Para te ajudar da melhor forma, preciso fazer uma pequena simulação. Posso seguir?"
            )
        elif resposta == "3":
            atualizar_estado(lead_id, "aguardando_simulacao")
            return (
                "Ótimo! Para agendarmos sua visita, preciso que você envie a carta de crédito ou a simulação via WhatsApp.\n"
                "Caso não tenha em mãos, podemos fazer uma nova simulação aqui mesmo. O que prefere?"
            )

    if estado == "coletando_dados":
        idx = obter_pergunta_atual(lead_id)

        if idx == 0:
            if pergunta.strip().lower() not in ["sim", "pode", "sim pode", "pode sim"]:
                return (
                    "Desculpa, não entendi. Posso fazer a simulação pra você? É só responder com 'sim' ou 'não', por favor."
                )
            avancar_pergunta(lead_id)
            return f"digitando...\n{perguntas_simulacao[0]}"

        adicionar_ao_historico(lead_id, "user", pergunta)
        pergunta_atual = obter_pergunta_atual(lead_id)
        avancar_pergunta(lead_id)

        if pergunta_atual is None:
            atualizar_estado(lead_id, "aguardando_simulacao")
            return (
                "Perfeito! Já coletei tudo que preciso.\n"
                "Vou preparar a simulação com base nesses dados e te aviso por aqui mesmo, tudo bem?"
            )

        return f"digitando...\n{pergunta_atual}"

    instrucoes_sistema = """
Você é Bruna, uma agente virtual inteligente especializada em imóveis do programa Minha Casa Minha Vida. Seu papel é conduzir o atendimento de forma empática e inteligente, entendendo o contexto da conversa.

REGRAS DE CONDUTA:
- Nunca entregue o endereço do imóvel (diga apenas "próximo ao Bairro Geisel").
- Envie três fotos do imóvel após a apresentação textual, simulando pausas como se estivesse digitando.
- Apresente as opções iniciais:
  1) É a primeira vez que tento comprar meu imóvel próprio
  2) Já tentei outras vezes e não consegui
  3) Já tenho carta aprovada e quero visitar o imóvel
- Se a opção for 3, solicite a carta de crédito ou simulação via WhatsApp.
- Se a opção for 1 ou 2, peça confirmação para iniciar a simulação.
- Só inicie a coleta de dados se o lead confirmar.
- Faça uma pergunta por vez.

Perguntas da simulação:
1. Quem vai financiar o imóvel com você? (Só você, com cônjuge, ou mais alguém?)
2. Como é a forma de trabalho da(s) pessoa(s) que irá/irão financiar? (Carteira assinada, autônomo, MEI...)
3. Qual é a renda familiar mensal total comprovada?
4. Vocês têm ao menos 3 anos de carteira assinada (mesmo que somando diferentes empregos)?
5. Qual a data de nascimento da pessoa que nasceu primeiro entre vocês?
6. Vocês têm filhos ou outras pessoas que dependem financeiramente de vocês?
7. Têm algum valor disponível para dar de entrada? (Pode usar FGTS)
"""

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

        return conteudo

    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

