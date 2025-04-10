from fastapi import APIRouter
from app.services.chat import obter_resposta

router = APIRouter()

@router.post("/")
def perguntar(mensagem: dict):
    resposta = obter_resposta(mensagem["mensagem"])
    return {"resposta": resposta}
