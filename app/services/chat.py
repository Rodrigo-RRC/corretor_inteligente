from fastapi import APIRouter, Request
from app.core.estado_lead import (
    estado_por_lead,
    perguntas_simulacao,
    inicializar_lead,
    obter_estado,
    avancar_pergunta
)
from app.core.info_mcmv import resposta_info_mcmv
from app.core.info_imovel import resposta_info_imovel

router = APIRouter()

@router.post("/chat/{lead_id}")
async def chat_bruna(lead_id: str, request: Request):
    dados = await request.json()
    mensagem = dados.get("mensagem", "").strip().lower()

    if lead_id not in estado_por_lead:
        inicializar_lead(lead_id)

    estado = obter_estado(lead_id)
    estado_atual = estado["estado"]
    chat_history = estado["chat_history"]
    pergunta_atual = estado["pergunta_atual"]
    intencao = estado.get("intencao", None)
    pausa_simulacao = estado.get("pausa_simulacao", False)

    resposta = ""

    def transicionar(novo_estado, nova_intencao=None):
        estado["estado"] = novo_estado
        if nova_intencao is not None:
            estado["intencao"] = nova_intencao

    def retomar_simulacao():
        estado["pausa_simulacao"] = False
        estado["estado"] = "coletando_dados"

    chat_history.append({"usuario": mensagem})

    # 🔹 Gatilhos inteligentes fora do fluxo
    if any(p in mensagem for p in ["mcmv", "minha casa", "subsídio", "programa"]):
        resposta = resposta_info_mcmv()
        estado["pausa_simulacao"] = True
        chat_history.append({"bruna": resposta})
        return {"resposta": resposta}

    if any(p in mensagem for p in ["endereço", "localização", "bairro", "metragem", "quartos", "banheiros", "vaga", "imóvel"]):
        resposta = resposta_info_imovel()
        estado["pausa_simulacao"] = True
        chat_history.append({"bruna": resposta})
        return {"resposta": resposta}

    if pausa_simulacao:
        retomar_simulacao()

    # 🔹 FSM: Atendimento fluido e empático
    if estado_atual == "apresentacao":
        resposta = (
            "Olá! Que bom te ver por aqui 😊\n"
            "Eu sou a Bruna, sua assistente no programa Minha Casa Minha Vida.\n\n"
            "Tenho um imóvel que pode ser exatamente o que você procura:\n\n"
            f"{resposta_info_imovel()}\n\n"
            "📸 [Foto 1]\n📸 [Foto 2]\n📸 [Foto 3]\n\n"
            "Agora me diga qual dessas opções melhor descreve você:\n"
            "1️⃣ É a primeira vez que tento comprar meu imóvel próprio\n"
            "2️⃣ Já tentei comprar e não consegui\n"
            "3️⃣ Já tenho carta aprovada e quero visitar o imóvel"
        )
        transicionar("esperando_resposta_opcao")

    elif estado_atual == "esperando_resposta_opcao":
        if "1" in mensagem:
            resposta = "Perfeito! Para te ajudar da melhor forma, preciso fazer uma pequena simulação. Pode ser?"
            transicionar("esperando_confirmacao_simulacao", "simulacao_opcao_1")
        elif "2" in mensagem:
            resposta = "Entendo… muitos clientes passaram por isso também. Vamos tentar juntos agora? Posso fazer uma simulação pra te ajudar?"
            transicionar("esperando_confirmacao_simulacao", "simulacao_opcao_2")
        elif "3" in mensagem:
            resposta = (
                "Ótimo! Pode me enviar sua carta de crédito ou simulação aprovada via WhatsApp?\n"
                "Se não tiver, posso fazer uma simulação aqui mesmo."
            )
            transicionar("esperando_confirmacao_simulacao", "verificar_documento")
        else:
            resposta = "Não entendi sua escolha. Você pode digitar 1, 2 ou 3?"

    elif estado_atual == "esperando_confirmacao_simulacao":
        if any(p in mensagem for p in ["sim", "pode", "claro", "vamos", "ok"]):
            if intencao == "verificar_documento":
                resposta = "Tudo bem, então vou precisar fazer uma nova simulação. Vamos começar?"
                transicionar("coletando_dados", "simulacao_nova")
            else:
                resposta = "Perfeito, então vamos começar nossa simulação!"
                transicionar("coletando_dados", intencao)
        else:
            resposta = "Se preferir, podemos conversar mais depois. É só me chamar."

    elif estado_atual == "coletando_dados":
        if pergunta_atual < len(perguntas_simulacao):
            resposta = perguntas_simulacao[pergunta_atual]
            avancar_pergunta(lead_id)
        else:
            resposta = "Obrigada! Agora vou processar os dados e em breve te envio a simulação!"
            transicionar("aguardando_simulacao")

    elif estado_atual == "aguardando_simulacao":
        resposta = "Estou aguardando a simulação. Assim que estiver pronta, envio para você!"

    chat_history.append({"bruna": resposta})
    return {"resposta": resposta}

