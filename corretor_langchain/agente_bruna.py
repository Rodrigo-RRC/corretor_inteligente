# agente_bruna.py

# 1. Importações essenciais do LangChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

# 2. Carrega variáveis do .env (API da OpenAI, por exemplo)
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# 3. Inicializa o modelo LLM com temperatura baixa (respostas mais estáveis)
llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.3)

# 4. Cria uma memória de conversa simples (buffer linear)
memory = ConversationBufferMemory()

# 5. Monta o agente com LLM + memória
bruna = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True  # Mostra detalhes da execução no terminal
)

# 6. Laço principal: simula o atendimento contínuo
if __name__ == "__main__":
    print("Bruna está pronta para atender. Digite sua mensagem:")
    while True:
        entrada = input("Você: ")
        resposta = bruna.run(entrada)
        print(f"Bruna: {resposta}")
