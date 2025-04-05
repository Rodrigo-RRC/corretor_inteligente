from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.post("/mensagem")
async def receber_mensagem(request: Request):
    corpo = await request.json()
    mensagem = corpo.get("mensagem", "").lower()

    print("Mensagem recebida:", mensagem)

    if "informações" in mensagem or "imóvel" in mensagem:
        time.sleep(1)
        return {"resposta": "Oi! Que bom que você se interessou por esse imóvel."}

    if "quero saber mais" in mensagem:
        time.sleep(1.5)
        return {"resposta": "Esse imóvel tem 2 quartos, fica perto do centro e aceita financiamento."}

    if "simulação" in mensagem:
        time.sleep(1.5)
        return {"resposta": "Para fazermos a simulação, preciso de algumas informações. Vamos começar pela sua idade?"}

    if "30" in mensagem or "anos" in mensagem:
        time.sleep(1.5)
        return {"resposta": "Perfeito. E qual é sua renda mensal aproximada?"}

    if "renda" in mensagem or "mil reais" in mensagem:
        time.sleep(1.5)
        return {"resposta": "Legal! Com base nessas informações, podemos seguir. Um corretor vai falar com você ainda hoje."}

    return {"resposta": "Desculpe, não entendi bem. Poderia repetir?"}
