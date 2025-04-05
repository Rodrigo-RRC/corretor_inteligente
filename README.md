# Corretor Inteligente

Este é um agente automatizado desenvolvido com FastAPI, projetado para responder clientes automaticamente via WhatsApp (usando UltraMsg), qualificando leads para imóveis específicos.

## Funcionalidades:
- Respostas humanizadas via API REST
- Simulação de digitação
- Coleta de dados do lead (idade, renda)
- Validação antes do contato com o corretor
- Preparado para integração com CRM e LLMs

## Tecnologias:
- Python
- FastAPI
- UltraMsg (WhatsApp API)
- AWS EC2 (hospedagem)

## Como rodar o projeto localmente:

```bash
git clone https://github.com/Rodrigo-RRC/corretor_inteligente.git
cd corretor_inteligente
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8001
