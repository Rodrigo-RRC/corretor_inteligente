# 📘 README_COMANDOS.md

## ✅ COMANDOS BÁSICOS – PROJETO CORRETOR INTELIGENTE

### 🔹 A) ACESSAR A INSTÂNCIA E A PASTA DO PROJETO
```bash
ssh -i SEU_ARQUIVO.pem ubuntu@SEU_IP_PUBLICO
cd ~/corretor_inteligente
source venv/bin/activate
```

### 🔹 B) COMANDOS PARA CRIAR OU EDITAR ARQUIVOS
```bash
nano nome_do_arquivo.py
```

#### ➤ Salvar e sair do editor `nano`:
CTRL + O → Salva o arquivo  
ENTER → Confirma o nome  
CTRL + X → Sai do editor

### 🔹 C) ENVIAR ARQUIVOS PARA O GITHUB (GIT PUSH)
```bash
git add nome_do_arquivo.py
git commit -m "Descrição do que foi alterado"
git push origin main
```

### 🔹 D) ATUALIZAR O CÓDIGO COM ALTERAÇÕES DO GITHUB (GIT PULL)
```bash
git pull origin main
```

### 🔹 E) RODAR O SERVIDOR FASTAPI COM UVICORN
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

#### ➤ (Opcional) Rodar o servidor dentro de uma `screen` chamada "corretor":
```bash
screen -S corretor
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

#### ➤ Sair da screen sem encerrar o servidor:
CTRL + A, depois D

#### ➤ Voltar para a screen:
```bash
screen -r corretor
```

### 🔹 F) TESTAR SUA API COM `curl`
```bash
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Qual o valor do imóvel?"}'
```

### 🔹 G) CRIAR O `requirements.txt` MANUALMENTE
```bash
nano requirements.txt
```

#### ➤ Conteúdo sugerido:
fastapi  
uvicorn  
python-dotenv  
requests

#### ➤ Salvar e enviar para o GitHub:
```bash
git add requirements.txt
git commit -m "Adiciona requirements.txt com dependências"
git push origin main
```

### 🔹 H) SOBRE O `curl`
Ferramenta de linha de comando para testar requisições HTTP.  
Útil para testar rapidamente se o bot está respondendo corretamente.  
Permite simular leads enviando mensagens à API do agente inteligente sem interface externa.

📌 Esses comandos são o kit de sobrevivência do seu projeto Corretor Inteligente.  
Rodrigo Ribeiro Carvalho — "Sem pressa. Mas com direção."
