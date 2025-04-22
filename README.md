---
title: Corretor Inteligente  
description: Agente virtual com IA para qualificação de leads no mercado imobiliário via WhatsApp, com foco em automação, coleta estruturada e integração com CRMs gratuitos e fluxos personalizados.  
---

# 🧠 Corretor Inteligente para o Mercado Imobiliário

Este projeto apresenta um **agente inteligente automatizado** para **qualificação de leads no WhatsApp**, voltado para corretores e imobiliárias que desejam otimizar o atendimento inicial por meio de uma jornada em três etapas:

1. **Coleta automatizada de dados essenciais** do lead para análise de financiamento;
2. **Pausa estratégica para envio da simulação** por parte do corretor humano;
3. **Retomada automatizada** do atendimento para agendamento de visita (com mensagens de confirmação em múltiplos estágios), ou encerramento cordial da conversa.

Utiliza IA generativa, WhatsApp API e integrações com CRMs gratuitos para manter um fluxo organizado e contínuo com os leads.

---

## 🚀 O que esta solução faz?

- **Responde de forma humanizada** às mensagens recebidas pelo WhatsApp  
- **Simula digitação**, trazendo naturalidade ao atendimento  
- **Coleta dados do lead**: idade, renda, dependentes, estado civil, FGTS, imóvel atual  
- **Gera base de dados estruturada para CRM gratuito ou planilha**  
- **Encaminha o lead para simulação manual do corretor**  
- **Retoma o atendimento** com mensagens automáticas para confirmação de visita  
- **Preparado para integração com LLMs e APIs externas**

---

## ⚙️ Tecnologias Utilizadas

- **Python** – para a lógica principal  
- **FastAPI** – criação da API REST  
- **UltraMsg (WhatsApp API)** – envio e recebimento de mensagens  
- **AWS EC2 (T2.micro)** – hospedagem  
- **Uvicorn** – servidor ASGI  
- **CRM Gratuito** – Bitrix24, HubSpot ou equivalente (em implantação)  

---

## 🧠 Exemplo de Conversa

```text
Bot: Olá! Tudo bem? Posso te ajudar com a simulação de financiamento. 😊
Antes disso, preciso te fazer algumas perguntas rápidas. Vamos lá?

Bot: Qual sua idade?
Bot: Obrigado! Agora, qual sua renda mensal (individual ou somada)?
Bot: Perfeito. Você possui pelo menos 3 anos de FGTS?

# Após coleta:
Bot: Ótimo! Agora o corretor vai fazer a simulação com base nesses dados.
Aguarde que em breve retornaremos! 🙌

# Retorno manual autorizado:
Bot: Rodrigo aqui novamente! Podemos agendar uma visita? Confirma esse número como seu WhatsApp?
```

---

## ☁️ Fluxo do Projeto

```mermaid
graph TD
A[Cliente envia mensagem no WhatsApp] --> B[API FastAPI recebe via UltraMsg]
B --> C[Lógica do Agente em Python]
C --> D[Coleta de dados estruturada]
D --> E[Pausa para simulação manual]
E --> F[Gatilho de retorno ativado no CRM ou planilha]
F --> G[Retomada automatizada para agendamento ou encerramento]
```

---

## ✅ Status Atual

- [x] Estrutura da API em FastAPI  
- [x] Função de simulação de digitação  
- [ ] Coleta de dados via fluxo interativo  
- [ ] Implementação da lógica de pausa + gatilho de retorno  
- [ ] Integração com CRM gratuito  
- [ ] Integração com Google Sheets  
- [ ] Integração com LLMs para respostas adaptativas

---

## 📁 Estrutura do Projeto

```
📦 corretor-inteligente
├── app/
│   ├── main.py               # FastAPI com rotas ativas
│   ├── chat.py               # Lógica de diálogo com o lead
│   ├── regras.py             # Regras do MCMV, triagens e condições
│   └── utils.py              # Funções auxiliares e simulador de digitação
```

---

## 🔧 Como Executar Localmente

```bash
# 1. Criar ambiente virtual (opcional, mas recomendado)
python3 -m venv venv
source venv/bin/activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Rodar a aplicação FastAPI
uvicorn main:app --host 0.0.0.0 --port 8001
```

---

## ⏭️ Próximas Etapas

- Aprimorar o fluxo com ramificações de perfil  
- Conectar com planilhas Google e CRM gratuito  
- Implementar mensagens por tipo de perfil  
- Integração com LLM para personalização mais avançada

---

<p align="center">
  <a href="https://rodrigo-rrc.github.io/Projetos_IA/" target="_blank">
    <img src="https://img.shields.io/badge/⬅️ Voltar para o índice interativo-blue?style=for-the-badge" alt="Voltar para o índice interativo"/>
  </a>
</p>

---

## 👨‍💻 Autor

**Rodrigo Ribeiro Carvalho**  
GitHub: [Rodrigo-RRC](https://github.com/Rodrigo-RRC)  
LinkedIn: [linkedin.com/in/rodrigo-ribeiro-datascience](https://linkedin.com/in/rodrigo-ribeiro-datascience)  
WhatsApp: [Clique aqui para conversar](https://wa.me/5547991820339)

---

## ✅ Licença

Este projeto é de uso livre e educacional. A comercialização só é permitida com autorização expressa do autor.
