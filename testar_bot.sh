#!/bin/bash

echo "Teste 1: Pergunta sobre imóvel no nome"
curl -X POST http://localhost:8000/ \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Tenho imóvel no meu nome, posso comprar pelo Minha Casa Minha Vida?"}'
echo -e "\n--------------------------\n"

echo "Teste 2: Pergunta sobre características do imóvel"
curl -X POST http://localhost:8000/ \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Quais são as características do imóvel?"}'
echo -e "\n--------------------------\n"

echo "Teste 3: Pergunta sobre valor do imóvel"
curl -X POST http://localhost:8000/ \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Qual o valor do imóvel?"}'
echo -e "\n--------------------------\n"
