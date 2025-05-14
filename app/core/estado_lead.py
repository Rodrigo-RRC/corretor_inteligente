estado_por_lead = {}

def inicializar_lead(lead_id):
    estado_por_lead[lead_id] = {
        "estado": "apresentacao",
        "chat_history": []
    }

def atualizar_estado(lead_id, novo_estado):
    if lead_id in estado_por_lead:
        estado_por_lead[lead_id]["estado"] = novo_estado

def obter_estado(lead_id):
    return estado_por_lead.get(lead_id, {}).get("estado", None)

def adicionar_ao_historico(lead_id, role, conteudo):
    if lead_id in estado_por_lead:
        estado_por_lead[lead_id]["chat_history"].append({"role": role, "content": conteudo})

def obter_historico(lead_id):
    return estado_por_lead.get(lead_id, {}).get("chat_history", [])
