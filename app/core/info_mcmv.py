# app/core/info_mcmv.py

info_mcmv = {
    "descricao": "Programa habitacional do governo federal voltado para famílias de baixa renda.",
    
    "regras": {
        "subsidio_sem_fgts_3_anos": True,
        "restricao_imovel_registrado": True,
        "comprovante_endereco_obrigatorio": True,
        "detalhes": [
            "Não é obrigatório ter 3 anos de FGTS para conseguir subsídio.",
            "Se o cliente já possui um imóvel registrado no nome, não poderá usar o programa.",
            "É necessário apresentar comprovante de endereço da cidade onde deseja comprar o imóvel."
        ]
    },

    "publico_alvo": "Famílias com renda mensal de até R$ 8.000,00, incluindo composição familiar.",
    
    "uso_fgts": (
        "É permitido usar o FGTS para entrada desde que o comprador tenha no mínimo 3 anos de carteira assinada, "
        "não tenha outro imóvel no nome e nunca tenha utilizado o FGTS em um financiamento anterior."
    ),

    "entrada": (
        "A entrada pode ser reduzida com o uso de subsídio do Governo Federal. "
        "Em alguns casos, é possível comprar com zero de entrada, dependendo da renda e do valor do imóvel."
    ),

    "subsídio": (
        "O subsídio pode chegar a até R$ 55.000,00, dependendo da faixa de renda e da localidade. "
        "É uma ajuda direta para reduzir o valor financiado."
    ),

    "faixas": {
        "Faixa 1": "Renda de até R$ 2.640,00",
        "Faixa 2": "Renda entre R$ 2.640,01 e R$ 4.400,00",
        "Faixa 3": "Renda entre R$ 4.400,01 e R$ 8.000,00"
    },

    "documentacao_necessaria": [
        "RG e CPF",
        "Comprovante de renda atualizado",
        "Comprovante de residência recente",
        "Carteira de trabalho e extrato do FGTS (caso utilize)",
        "Certidão de nascimento ou casamento"
    ],

    "orientacao_final": "Em caso de dúvidas, consulte um corretor credenciado ou entre em contato com a Caixa Econômica Federal."
}

