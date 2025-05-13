#!/bin/bash

echo "==== TESTE DE CONVERSA COM A BRUNA ===="

# Entrada inicial simulando o clique no anúncio
echo -e "\n[LEAD] Oi"
sleep 1

# Abertura da Bruna
echo -e "\n[BRUNA] Olá! Sou a Bruna, sua corretora virtual — uma agente inteligente aqui pra te ajudar com imóveis do Minha Casa Minha Vida."
echo "[BRUNA] Este imóvel fica próximo ao Bairro Geisel, tem 1 suíte + 1 quarto, área de lazer completa, e está saindo a partir de R\$ 178 mil."
echo "[BRUNA] Posso te ajudar de duas formas:"
echo "[BRUNA] 1) Ver se o imóvel combina com seu perfil"
echo "[BRUNA] 2) Agendar uma visita (preciso antes fazer uma pré-análise)"
echo "[BRUNA] Com o que você gostaria de começar?"
sleep 2

# Simulando escolha do lead
echo -e "\n[LEAD] Quero ver se combina com meu perfil"
sleep 1

# Primeira pergunta adaptativa
echo -e "\n[BRUNA] Você pretende financiar esse imóvel?"
sleep 1
echo -e "[LEAD] Sim"

echo -e "\n[BRUNA] Você possui algum imóvel em seu nome?"
sleep 1
echo -e "[LEAD] Não"

echo -e "\n[BRUNA] Seu estado civil é casado(a) no papel ou solteiro(a)?"
sleep 1
echo -e "[LEAD] Casado"

echo -e "\n[BRUNA] Entendi! Como vocês são casados no papel, o financiamento será feito em conjunto — ou seja, os dois precisam assinar o contrato, tudo bem?"
sleep 1
echo -e "[LEAD] Tudo bem"

echo -e "\n[BRUNA] Qual sua data de nascimento?"
sleep 1
echo -e "[LEAD] 12/04/1987"

echo -e "\n[BRUNA] Tem ao menos 3 anos de FGTS acumulado na vida?"
sleep 1
echo -e "[LEAD] Sim"

echo -e "\n[BRUNA] Tem filhos ou dependentes financeiros?"
sleep 1
echo -e "[LEAD] Tenho 2 filhos"

echo -e "\n[BRUNA] Qual é sua renda familiar mensal total?"
sleep 1
echo -e "[LEAD] R\$ 2.800"

echo -e "\n[BRUNA] Como você recebe sua renda? (Carteira assinada, MEI, informal...)"
sleep 1
echo -e "[LEAD] MEI"

echo -e "\n[BRUNA] Tem algum valor guardado para entrada? Pretende usar FGTS?"
sleep 1
echo -e "[LEAD] Tenho FGTS e R\$ 5 mil guardado"

# Encerramento da coleta
echo -e "\n[BRUNA] Perfeito! Já coletei tudo que preciso."
echo "[BRUNA] Vou preparar uma simulação com base nesses dados e te aviso por aqui mesmo assim que ela estiver pronta, tudo bem?"

echo -e "\n==== FIM DO TESTE ===="

