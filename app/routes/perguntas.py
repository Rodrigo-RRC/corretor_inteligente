from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def perguntar(payload: dict):
    mensagem = payload.get("mensagem")
    lead_id = payload.get("lead_id", "lead_padrao")  # usa "lead_padrao" se não enviar

    resposta = obter_resposta(mensagem, lead_id)
    return {"resposta": resposta}

