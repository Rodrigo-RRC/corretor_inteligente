# 📘 README_COMANDOS.md

## ✅ COMANDOS COMPLETOS – PROJETO CORRETOR INTELIGENTE (ATUALIZADO E DEFINITIVO)

🔹 A) ACESSAR A INSTÂNCIA EC2 E ATIVAR O PROJETO  
ssh -i SEU_ARQUIVO.pem ubuntu@SEU_IP_PUBLICO  
cd ~/corretor_inteligente  
source venv/bin/activate  

🔹 B) ATUALIZAR O SISTEMA OPERACIONAL (APT UPDATE/UPGRADE)  
sudo apt update  
sudo apt upgrade -y  
sudo reboot  

➤ Verificar versão do kernel:  
uname -r  

🔹 C) COMANDOS PARA CRIAR OU EDITAR ARQUIVOS  
nano nome_do_arquivo.py  

➤ Atalhos no nano:  
CTRL + O → Salva o arquivo  
ENTER → Confirma o nome  
CTRL + X → Sai do editor  

🔹 D) USO DO GIT – COMANDOS ESSENCIAIS  
git status  
git add nome_do_arquivo.py  
git commit -m "Descrição clara da alteração"  
git push origin main  
git pull origin main  

🔹 E) RODAR A APLICAÇÃO COM UVICORN  
uvicorn app.main:app --host 0.0.0.0 --port 8000  

🔹 F) USAR SCREEN PARA RODAR EM SEGUNDO PLANO  
screen -S corretor  
uvicorn app.main:app --host 0.0.0.0 --port 8000  

➤ Sair da screen sem parar o servidor:  
CTRL + A, depois D  

➤ Voltar para a screen:  
screen -r corretor  

➤ Encerrar a screen de forma definitiva:  
1. Reanexe com:  
   screen -r corretor  
2. Pare o processo com:  
   CTRL + C  
3. Finalize com:  
   exit  

✅ A screen será encerrada e não ficará mais ativa em background.

🔹 G) TESTAR SUA API COM `curl` (versão simples)  
curl -X POST http://localhost:8000/ \  
  -H "Content-Type: application/json" \  
  -d '{"mensagem": "Qual o valor do imóvel?"}'

🔹 H) CRIAR E MANTER O `requirements.txt`  
nano requirements.txt  

➤ Conteúdo sugerido:  
fastapi  
uvicorn  
python-dotenv  
requests  

➤ Versionar no Git:  
git add requirements.txt  
git commit -m "Atualiza dependências do projeto"  
git push origin main  

🔹 I) EDITAR O `chat.py` COM `nano`  
nano app/services/chat.py  

🔹 J) EXTRAS ÚTEIS  
➤ Verificar status de serviços do Ubuntu:  
sudo pro status  

➤ Ver pacotes que podem ser atualizados:  
apt list --upgradable  

➤ Atualizar pacotes com segurança:  
sudo apt update && sudo apt upgrade -y  

🔹 K) SAIR DA INSTÂNCIA E ECONOMIZAR CUSTO NA AWS  
➤ Encerrar a sessão corretamente:  
deactivate  
exit  

➤ Para desligar a instância (e não gastar enquanto estiver fora):  
sudo shutdown now  

🔹 L) GIT – COMO RESOLVER ERRO DE PUSH (rejected push)  
➤ Quando aparecer erro de push (ex: `fetch first`), rode:  
git pull origin main --no-rebase  

➤ Se abrir o editor nano para merge:  
CTRL + O → ENTER → CTRL + X  

➤ Depois finalize com:  
git push origin main  

🔹 M) SAIR DO `nano` SEM SALVAR  
➤ Pressione: CTRL + X  
➤ Responda com: N  

🔹 N) CONTROLE DE ESTADO E TESTES COM `lead_id`  
➤ Verificar se o `estado_lead.py` foi salvo corretamente:  
ls app/core  

➤ Criar ou editar arquivos de lógica do agente:  
nano app/core/estado_lead.py  
nano app/services/chat.py  
nano app/routes/perguntas.py  

➤ Executar a API FastAPI com caminho correto:  
uvicorn app.main:app --reload  

➤ Testar com `curl` enviando o `lead_id`:  
curl -X POST http://127.0.0.1:8000/ \  
  -H "Content-Type: application/json" \  
  -d '{"mensagem": "Oi", "lead_id": "11999999999"}'  

➤ Simular resposta da IA após simulação manual:  
curl -X POST http://127.0.0.1:8000/ \  
  -H "Content-Type: application/json" \  
  -d '{"mensagem": "#resposta_simulacao:11999999999:Rodrigo, com base nos seus dados a simulação foi aprovada!", "lead_id": "11999999999"}'  

➤ Encerrar o servidor Uvicorn:  
CTRL + C  

📌 Esses comandos são fundamentais para manter o controle por lead, os estados da conversa e a pausa entre coleta e simulação.  
Atualize este bloco conforme o agente evoluir.

---

📌 **Este é o guia oficial de sobrevivência do projeto Corretor Inteligente.**  
Atualizado, funcional, definitivo.  
Rodrigo Ribeiro Carvalho — "Sem pressa. Mas com direção."
