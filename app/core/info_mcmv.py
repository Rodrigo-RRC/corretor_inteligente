info_mcmv = {
    "descricao": "Programa habitacional do governo federal que facilita o acesso à casa própria para famílias de baixa e média renda.",
    "publico_alvo": "Famílias com renda mensal de até R$ 12.000,00 (área urbana).",
    "uso_fgts": (
        "É permitido usar o FGTS como entrada, desde que o comprador tenha ao menos 3 anos de carteira assinada, "
        "não possua outro imóvel residencial em seu nome e não tenha usado o FGTS anteriormente em financiamento habitacional."
    ),
    "entrada": (
        "O valor da entrada depende da renda, da localização e do perfil familiar. "
        "Pode ser reduzido ou zerado com o uso de subsídio e FGTS, mas só é possível saber após uma simulação personalizada."
    ),
    "subsídio": (
        "O governo pode conceder subsídio de até R$ 55.000,00, que reduz diretamente o valor a ser financiado. "
        "O valor exato depende da faixa de renda e da cidade onde o imóvel está localizado."
    ),
    "faixas": {
        "Faixa 1": "Renda até R$ 2.850,00 — maiores subsídios e menores taxas de juros.",
        "Faixa 2": "Renda entre R$ 2.850,01 e R$ 4.700,00 — condições intermediárias.",
        "Faixa 3": "Renda entre R$ 4.700,01 e R$ 8.600,00 — juros reduzidos, sem subsídio.",
        "Faixa 4": "Renda entre R$ 8.600,01 e R$ 12.000,00 — financiamento permitido, sem subsídio, com taxa de juros de até 10% ao ano."
    },
    "documentacao_necessaria": [
        "RG e CPF",
        "Comprovante de renda atualizado",
        "Comprovante de residência recente",
        "Carteira de trabalho (se CLT) ou extrato do MEI/autônomo",
        "Extrato do FGTS (se for utilizar)",
        "Certidão de nascimento ou casamento (se aplicável)"
    ],
    "prioridade_mulheres": (
        "O programa dá preferência para registro do imóvel em nome da mulher, mesmo sem autorização do cônjuge."
    ),
    "fgts_futuro": (
        "Existe a possibilidade de utilizar o FGTS Futuro, permitindo o uso dos depósitos futuros do fundo para abater parcelas mensais do financiamento."
    ),
    "orientacao_final": (
        "A simulação personalizada é essencial para descobrir se há subsídio disponível e qual o valor mínimo de entrada. "
        "A análise final é feita exclusivamente pela Caixa Econômica Federal."
    )
}


def resposta_info_mcmv():
    return (
        f"{info_mcmv['descricao']}\n\n"
        f"👥 Público-alvo: {info_mcmv['publico_alvo']}\n\n"
        f"🏠 Uso do FGTS: {info_mcmv['uso_fgts']}\n\n"
        f"💰 Entrada: {info_mcmv['entrada']}\n\n"
        f"🎯 Subsídio: {info_mcmv['subsídio']}\n\n"
        "📊 Faixas de renda:\n" +
        "\n".join([f"- {faixa}: {descricao}" for faixa, descricao in info_mcmv["faixas"].items()]) +
        "\n\n📄 Documentação necessária:\n" +
        "\n".join([f"- {doc}" for doc in info_mcmv["documentacao_necessaria"]]) +
        f"\n\n👩 Prioridade: {info_mcmv['prioridade_mulheres']}\n\n"
        f"📈 FGTS Futuro: {info_mcmv['fgts_futuro']}\n\n"
        f"📌 Observação final: {info_mcmv['orientacao_final']}"
    )

