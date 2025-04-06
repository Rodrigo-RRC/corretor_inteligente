from contexto_mcmv import info_mcmv
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente (.env)
load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Inicializa o app FastAPI
app = FastAPI()

# Configura o modelo da Hugging Face
llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature": 0.7})

# Prompt base para a IA gerar respostas
prompt = PromptTemplate(
    input_variables=["mensagem"],
    template=f"""
Você é Alex, assistente virtual do corretor Rodrigo Ribeiro Carvalho.

Com base nas informações abaixo, responda de forma clara, educada e objetiva à pergunta do usuário.

Informações oficiais do programa Minha Casa Minha Vida:
{info_mcmv}

Pergunta do usuário:
{{mensagem}}
"""
)

# Cria o encadeamento do agente
chain = LLMChain(llm=llm, prompt=prompt)

# Define o formato de entrada da API
class Mensagem(BaseModel):
    texto: str

# Rota para receber mensagens e responder com IA
@app.post("/mensagem")
def responder(pergunta: Mensagem):
    resposta = chain.run(mensagem=pergunta.texto)
    return {"resposta": resposta}

