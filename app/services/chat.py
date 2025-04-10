import os
from openai import OpenAI
from dotenv import load_dotenv
from app.core.info_imovel import informacoes_gerais
from app.core.info_mcmv import info_mcmv

# Carrega variáveis do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Memória simples para manter o histórico de conversa
chat_history = []

def obter_resposta(pergunta):
    # Instruções iniciais para orientar o comportamento da IA
    instrucoes_sistema = (
      f"Você é um assistente virtual especializado em vendas de imóveis populares. "
      f"Responda com simpatia e de forma curta, objetiva e adaptada ao público com baixa escolaridade. "
      f"O imóvel está localizado no bairro {informacoes_gerais['bairro']} e próximo de {', '.join(informacoes_gerais['proximidades'])}. "
      f"Descrição: {informacoes_gerais['descricao']}. "
      f"NUNCA revele o nome do imóvel, rua ou localização exata. "
      f"NÃO informe o valor antes da simulação. "
      f"Se a pergunta for sobre restrições no nome, diga: 'Se estiver com o nome sujo, é necessário regularizar antes de fazer o financiamento.' "
      f"Se a pessoa disser que já tem imóvel no nome, diga: 'Quem já tem imóvel registrado não pode participar do Minha Casa Minha Vida.' "
      f"Se perguntarem sobre documentos ou FGTS, use as regras do programa que estão descritas abaixo: "
      f"{info_mcmv['regras']['detalhes'][0]} | "
      f"{info_mcmv['regras']['detalhes'][1]} | "
      f"{info_mcmv['regras']['detalhes'][2]} "
      f"NUNCA escreva parágrafos longos ou com linguagem jurídica. Seja direto como um atendente popular."
)


    # Monta a lista de mensagens (contexto) para a API
    mensagens = [{"role": "system", "content": instrucoes_sistema}]
    mensagens.extend(chat_history)
    mensagens.append({"role": "user", "content": pergunta})

    try:
        # Chama a API da OpenAI com o contexto e a nova pergunta
        resposta = client.chat.completions.create(
            model="gpt-4",
            messages=mensagens,
            temperature=0.7
        )
        conteudo = resposta.choices[0].message.content.strip()

        # Atualiza o histórico de conversa
        chat_history.append({"role": "user", "content": pergunta})
        chat_history.append({"role": "assistant", "content": conteudo})

        return conteudo

    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

