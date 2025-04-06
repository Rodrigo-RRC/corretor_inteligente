# 📘 README_COMANDOS.md

## ✅ COMANDOS BÁSICOS – PROJETO CORRETOR INTELIGENTE

### 🔹 A) ACESSAR A INSTÂNCIA E A PASTA DO PROJETO
```bash
ssh -i SEU_ARQUIVO.pem ubuntu@SEU_IP_PUBLICO
cd ~/corretor_inteligente
source venv/bin/activate
```

---

### 🔹 B) COMANDOS PARA CRIAR OU EDITAR ARQUIVOS

#### ➤ Criar ou editar um arquivo
```bash
nano nome_do_arquivo.py
```

#### ➤ Salvar e sair do editor `nano`
- `CTRL + O` → Salva o arquivo
- `ENTER` → Confirma o nome
- `CTRL + X` → Sai do editor

---

### 🔹 C) ENVIAR ARQUIVOS PARA O GITHUB (GIT PUSH)

#### ➤ Adicionar um ou mais arquivos ao Git
```bash
git add nome_do_arquivo.py
```

#### ➤ Fazer o commit com uma mensagem descritiva
```bash
git commit -m "Descrição do que foi alterado"
```

#### ➤ Enviar para o repositório remoto (GitHub)
```bash
git push origin main
```

---

### 🔹 D) ATUALIZAR O SERVIDOR COM CÓDIGOS DO GITHUB (GIT PULL)

#### ➤ Puxar alterações feitas diretamente no GitHub
```bash
git pull origin main
```

---

### 🔹 E) RODAR O SERVIDOR FASTAPI COM UVICORN

#### ➤ Rodar o agente na porta 8000
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

#### ➤ (Opcional) Rodar dentro de uma `screen` chamada "corretor"
```bash
screen -S corretor
uvicorn main:app --host 0.0.0.0 --port 8000
```

#### ➤ Sair da screen sem parar o servidor
- `CTRL + A`, depois `D`

#### ➤ Voltar para a screen depois
```bash
screen -r corretor
```

---

### 🔹 F) TESTAR SUA API COM `curl`

#### ➤ Enviar uma mensagem simulada
```bash
curl -X POST http://localhost:8000/mensagem \
  -H "Content-Type: application/json" \
  -d '{"texto": "Qual o valor do imóvel?"}'
```

---

### 🔹 G) CRIAR O requirements.txt MANUALMENTE

#### ➤ Criar e editar o arquivo
```bash
nano requirements.txt
```

#### ➤ Conteúdo sugerido:
```
fastapi
uvicorn
langchain
transformers
python-dotenv
huggingface_hub
```

#### ➤ Salvar e subir para o GitHub
```bash
git add requirements.txt
git commit -m "Adiciona requirements.txt com dependências"
git push origin main
```

---

### 🔹 H) IMPORTANTE – SOBRE O `curl`
- Ferramenta de terminal para fazer requisições HTTP
- Serve para testar sua API **sem precisar de navegador ou WhatsApp**
- Simula um lead enviando uma pergunta diretamente para seu agente inteligente

---

📌 Tudo isso está ajustado para o projeto rodar direto na AWS, com integração ao GitHub e estrutura profissional.

Rodrigo Ribeiro Carvalho — "Sem pressa. Mas com direção."
