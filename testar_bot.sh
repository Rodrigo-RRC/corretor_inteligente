#!/bin/bash

echo "Teste 1: Lead curioso e direto"
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Oi, vi o anúncio. Onde fica exatamente esse apartamento?"}'
echo -e "\n--------------------------\n"

echo "Teste 2: Lead com perfil prático"
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Quero saber se consigo financiar mesmo com nome limpo, mas pouca renda."}'
echo -e "\n--------------------------\n"

echo "Teste 3: Lead perguntando o valor"
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Qual é o valor total do imóvel com tudo?"}'
echo -e "\n--------------------------\n"

echo "Teste 4: Lead desconfiado"
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Precisa pagar alguma coisa antes de fazer a simulação?"}'
echo -e "\n--------------------------\n"

echo "Teste 5: Lead objetivo e apressado"
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Sou autônomo, ganho R$ 3.000 por mês. Consigo?"}'
echo -e "\n--------------------------\n"

echo "Teste 6: Lead já com simulação"
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Já fiz a simulação. Posso agendar a visita direto?"}'
echo -e "\n--------------------------\n"

