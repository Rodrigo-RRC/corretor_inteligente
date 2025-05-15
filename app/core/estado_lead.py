estado_por_lead = {}

perguntas_simulacao = [
    "Quem vai financiar o imóvel com você? (Só você, com cônjuge, ou mais alguém?)",
    "Como é a forma de trabalho da(s) pessoa(s) que irá/irão financiar? (Carteira assinada, autônomo, MEI...)",
    "Qual é a renda familiar mensal total comprovada?",
    "Vocês têm ao menos 3 anos de carteira assinada (mesmo que somando diferentes empregos)?",
    "Qual a data de nascimento da pessoa que nasceu primeiro entre vocês?",
    "Vocês têm filhos ou outras pessoas que dependem financeiramente de vocês?",
    "Têm algum valor disponível para dar de entrada? (Pode usar FGTS)"
]

def inicializar_lead(lead_id):
    estado_por_lead[lead_id] = {
        "estado": "apresentacao",
        "chat_history": [],
        "pergunta_atual": 0
    }

def obter_estado(lead_id):
    return estado_por_lead.get(lead_id, {}).get("estado")

def atualizar_estado(lead_id, novo_estado):
    if lead_id in estado_por_lead:
        estado_por_lead[lead_id]["estado"] = novo_estado

def obter_historico(lead_id):
    return estado_por_lead.get(lead_id, {}).get("chat_history", [])

def adicionar_ao_historico(lead_id, role, content):
    if lead_id in estado_por_lead:
        estado_por_lead[lead_id]["chat_history"].append({"role": role, "content": content})

def obter_pergunta_atual(lead_id):
    idx = estado_por_lead.get(lead_id, {}).get("pergunta_atual", 0)
    if idx < len(perguntas_simulacao):
        return perguntas_simulacao[idx]
    return None

def avancar_pergunta(lead_id):
    if lead_id in estado_por_lead:
        estado_por_lead[lead_id]["pergunta_atual"] += 1

