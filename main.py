# Importa a biblioteca FastAPI para criar a API
from fastapi import FastAPI, Request

# Cria a instância do app
app = FastAPI()

# Dicionário para armazenar os estados da conversa (por número de telefone)
conversas = {}

# Lista com mensagens-padrão esperadas na entrada do lead (caso ele não apague o texto)
mensagens_padroes = [
    "olá! gostaria de receber mais informações do empreendimento.",
    "quero saber mais sobre o imóvel",
    "gostaria de mais detalhes"
]

# Rota principal que recebe mensagens via POST
@app.post("/mensagem")
async def receber_mensagem(request: Request):
    # Captura o corpo da requisição (mensagem enviada pelo lead)
    corpo = await request.json()
    numero = corpo.get("numero", "")       # Número do lead (simulado)
    mensagem = corpo.get("mensagem", "").strip().lower()  # Normaliza a mensagem recebida

    # Se ainda não existe conversa com esse número, criamos o início do histórico
    if numero not in conversas:
        conversas[numero] = {
            "etapa": "inicio",
            "dados": {}
        }

    # Verifica a etapa atual da conversa
    etapa = conversas[numero]["etapa"]

    # Se for o início da conversa
    if etapa == "inicio":
        if mensagem not in mensagens_padroes:
            # O lead escreveu algo diferente do esperado (ex: "quanto é?")
            conversas[numero]["etapa"] = "apresentacao"
            return {
                "resposta": (
                    "Claro! Esse imóvel tem ótimas condições. "
                    "Antes de te explicar melhor, posso me apresentar rapidinho?\n\n"
                    "Sou Alex, assistente virtual do corretor Rodrigo Ribeiro Carvalho. "
                    "Estou aqui pra te ajudar com todas as informações. Podemos começar?"
                )
            }
        else:
            # O lead enviou a mensagem padrão esperada
            conversas[numero]["etapa"] = "apresentacao"
            return {
                "resposta": (
                    "Oi! Sou Alex, assistente virtual do corretor Rodrigo Ribeiro Carvalho. "
                    "Estou aqui pra te ajudar com as informações e simulações do imóvel. Vamos nessa?\n\n"
                    "O imóvel fica no bairro Novo Geisel, possui 1 quarto e 1 suíte, "
                    "vaga de garagem descoberta e área de lazer completa.\n\n"
                    "Essas características te atendem?"
                )
            }

    # Se já passou da etapa de apresentação (futuro desenvolvimento)
    return {
        "resposta": "Legal! Em breve vou continuar essa conversa. Por enquanto, estamos testando a estrutura inicial 😄"
    }
