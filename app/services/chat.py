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
        f"Você é um assistente imobiliário simpático e objetivo, com foco em imóveis populares.\n"
        f"Informações do imóvel:\n"
        f"- Bairro: {informacoes_gerais['bairro']}\n"
        f"- Proximidades: {', '.join(informacoes_gerais['proximidades'])}\n"
        f"- Descrição: {informacoes_gerais['descricao']}\n"
        f"- Valor: {informacoes_gerais['valor']}\n\n"
        f"Regras:\n"
        f"- Nunca diga o nome do imóvel ou da rua.\n"
        f"- Pode informar o valor do imóvel se perguntarem, mas sempre destaque que o mais importante é a simulação de financiamento.\n"
        f"- Se o cliente disser que já tem uma simulação aprovada, peça para ele enviar. Se não enviar, diga educadamente que não é possível avançar sem ela.\n"
        f"- Caso a pergunta seja sobre o programa Minha Casa Minha Vida, use as seguintes regras:\n"
        f"  • {info_mcmv['regras']['detalhes'][0]}\n"
        f"  • {info_mcmv['regras']['detalhes'][1]}\n"
        f"  • {info_mcmv['regras']['detalhes'][2]}\n"
        f"- Nunca incentive o cliente a comprar se ele estiver com o nome sujo. Diga que é necessário regularizar primeiro.\n"
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

