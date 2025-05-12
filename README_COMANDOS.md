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

### 🔹 G) TESTAR SUA API COM `curl`
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

📌 **Este é o guia oficial de sobrevivência do projeto Corretor Inteligente.**  
Atualizado, funcional, definitivo.  
Rodrigo Ribeiro Carvalho — "Sem pressa. Mas com direção."
