#CÓDIGO JR
produtos = {
    "notebook": 3500,
    "mouse": 80,
    "teclado": 120
}

caros = {}

for nome, preco in produtos.items():
    if preco > 100:
        caros[nome] = preco


#CÓDIGO SR
caros = {n: p for n, p in produtos.items() if p > 100}
