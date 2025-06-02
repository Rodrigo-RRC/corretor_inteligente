
# app/core/info_imovel.py

informacoes_gerais = {
    "bairro": "Bairro Novo Geisel",
    "proximidades": [
        "Arena Esquerdinha",
        "Bairro Geisel e Bairro Cuiá",
        "Mercados e Hipermercados próximos"
    ],
    "descricao": "Imóvel com 1 suíte + 1 quarto, sala, cozinha, banheiro social e área de serviço. Condomínio fechado com segurança, área de lazer e excelente localização.",
    "valor": "R$ 178.000,00",
    "regras": {
        "mostrar_nome_imovel": False,
        "mostrar_rua": False,
        "mostrar_valor_apenas_apos_simulacao": False,
        "horario_resposta_limite": "22:00",
        "mensagem_digitando": True
    }
}


def resposta_info_imovel():
    texto = (
        f"📍 Localização: {informacoes_gerais['bairro']}\n\n"
        f"🛏️ Descrição: {informacoes_gerais['descricao']}\n\n"
        "🗺️ Nas proximidades:\n" +
        "\n".join([f"- {p}" for p in informacoes_gerais["proximidades"]])
    )

    if not informacoes_gerais["regras"]["mostrar_valor_apenas_apos_simulacao"]:
        texto += f"\n\n💰 Valor: {informacoes_gerais['valor']}"

    return texto

