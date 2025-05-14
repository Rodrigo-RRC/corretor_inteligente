# 📘 README_COMANDOS.md

## ✅ COMANDOS COMPLETOS – PROJETO CORRETOR INTELIGENTE (ATUALIZADO E DEFINITIVO)

### 🔹 A) ACESSAR A INSTÂNCIA EC2 E ATIVAR O PROJETO
```bash
ssh -i SEU_ARQUIVO.pem ubuntu@SEU_IP_PUBLICO
cd ~/corretor_inteligente
source venv/bin/activate
```

---

### 🔹 B) ATUALIZAR O SISTEMA OPERACIONAL (APT UPDATE/UPGRADE)
```bash
sudo apt update
sudo apt upgrade -y
```

#### ➤ Após atualização completa:
```bash
sudo reboot
```

#### ➤ Verificar versão do kernel:
```bash
uname -r
```

---

### 🔹 C) COMANDOS PARA CRIAR OU EDITAR ARQUIVOS
```bash
nano nome_do_arquivo.py
```

#### ➤ Atalhos no `nano`:
CTRL + O → Salva o arquivo  
ENTER → Confirma o nome  
CTRL + X → Sai do editor  

---

### 🔹 D) USO DO GIT – COMANDOS ESSENCIAIS
```bash
git status
git add nome_do_arquivo.py
git commit -m "Descrição clara da alteração"
git push origin main
git pull origin main
```

---

### 🔹 E) RODAR A APLICAÇÃO COM UVICORN
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

### 🔹 F) USAR SCREEN PARA RODAR EM SEGUNDO PLANO
```bash
screen -S corretor
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

#### ➤ Sair da screen sem parar o servidor:
CTRL + A, depois D

#### ➤ Voltar para a screen:
```bash
screen -r corretor
```

---

### 🔹 G) TESTAR SUA API COM `curl` (versão simples)
```bash
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Qual o valor do imóvel?"}'
```

---

### 🔹 H) CRIAR E MANTER O `requirements.txt`
```bash
nano requirements.txt
```

#### ➤ Conteúdo sugerido:
fastapi  
uvicorn  
python-dotenv  
requests  

#### ➤ Versionar no Git:
```bash
git add requirements.txt
git commit -m "Atualiza dependências do projeto"
git push origin main
```

---

### 🔹 I) EDITAR O `chat.py` COM `nano`
```bash
nano app/services/chat.py
```

---

### 🔹 J) EXTRAS ÚTEIS

#### ➤ Verificar status de serviços do Ubuntu:
```bash
sudo pro status
```

#### ➤ Ver pacotes que podem ser atualizados:
```bash
apt list --upgradable
```

#### ➤ Atualizar pacotes com segurança:
```bash
sudo apt update && sudo apt upgrade -y
```

---

### 🔹 K) SAIR DA INSTÂNCIA E ECONOMIZAR CUSTO NA AWS

#### ✅ Encerrar a sessão corretamente:
```bash
deactivate     # Sai do ambiente virtual Python
exit           # Encerra a sessão SSH do PuTTY
```

#### ✅ Para desligar a instância (e não gastar enquanto estiver fora):
```bash
sudo shutdown now
```

---

### 🔹 L) GIT – COMO RESOLVER ERRO DE PUSH (rejected push)

#### ➤ Quando aparecer erro de push (ex: `fetch first`), rode:
```bash
git pull origin main --no-rebase
```

#### ➤ Se abrir o editor `nano` para merge, apenas:
CTRL + O → ENTER → CTRL + X

#### ➤ Depois finalize com:
```bash
git push origin main
```

---

### 🔹 M) SAIR DO `nano` SEM SALVAR
Se abrir o `nano` por engano e quiser sair sem alterar nada:

1. Pressione:
```
CTRL + X
```

2. Quando for perguntado:
```
Save modified buffer? (ANSWERING "No" WILL DESTROY CHANGES)
```
Responda com:
```
N
```

---

### 🔹 N) CONTROLE DE ESTADO E TESTES COM `lead_id`

#### ➤ Verificar se o `estado_lead.py` foi salvo corretamente:
```bash
ls app/core
```

#### ➤ Criar ou editar arquivos de lógica do agente:
```bash
nano app/core/estado_lead.py
nano app/services/chat.py
nano app/routes/perguntas.py
```

#### ➤ Executar a API FastAPI com caminho correto:
```bash
uvicorn app.main:app --reload
```

#### ➤ Testar com `curl` enviando o `lead_id`:
```bash
curl -X POST http://127.0.0.1:8000/ \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Oi", "lead_id": "11999999999"}'
```

#### ➤ Simular resposta da IA após simulação manual:
```bash
curl -X POST http://127.0.0.1:8000/ \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "#resposta_simulacao:11999999999:Rodrigo, com base nos seus dados a simulação foi aprovada!", "lead_id": "11999999999"}'
```

#### ➤ Encerrar o servidor Uvicorn:
```
CTRL + C
```

📌 Esses comandos são fundamentais para manter o controle por lead, os estados da conversa e a pausa entre coleta e simulação.  
Atualize este bloco conforme o agente evoluir.

---

📌 **Este é o guia oficial de sobrevivência do projeto Corretor Inteligente.**  
Atualizado, funcional, definitivo.  
Rodrigo Ribeiro Carvalho — "Sem pressa. Mas com direção."
