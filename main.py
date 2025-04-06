from fastapi import FastAPI
from pydantic import BaseModel
from langchain.llms import HuggingFaceHub
from langchain import LLMChain, PromptTemplate
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente (.env)
load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Inicializa o app FastAPI
app = FastAPI()

# Configura o modelo da Hugging Face
llm = HuggingFaceHub(
    repo_id="google/flan-t5-large",
    model_kwargs={"temperature": 0.7, "max_length": 256}
)

# Prompt base para a IA gerar respostas
prompt = PromptTemplate(
    input_variables=["mensagem"],
    template="Responda de forma clara, educada e objetiva a esta pergunta: {mensagem}"
)

# Cria o encadeamento do agente
chain = LLMChain(llm=llm, prompt=prompt)

# Define o formato de entrada da API
class Mensagem(BaseModel):
    texto: str

# Rota para receber mensagens e responder com IA
@app.post("/mensagem")
async def responder(mensagem: Mensagem):
    pergunta = mensagem.texto
    resposta = chain.run(mensagem=pergunta)
    return {"resposta": resposta}

