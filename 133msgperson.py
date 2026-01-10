dados_clientes = {
    "Joao": {"Valor Mês": 500.0, "Giftbonus": 100.0},
    "Alvaro": {"Valor Mês": 300.0, "Giftbonus": 60.00}
}

for nome, dados in dados_clientes.items():

    mensagem = f"""
Bom dia {nome}! Muito obrigado por comprar conosco neste último mês! 

Como forma de agradecimento, estamos disponibilizando um Giftbônus para você de R$ {dados['Giftbonus']}.
---------------------------------------------------"""
    print(mensagem)

