import requests
from bs4 import BeautifulSoup
from datetime import datetime


def obter_valor(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    valor = soup.find("fin-streamer", {"data-test": "qsp-price"})
    return valor.text if valor else "Não encontrado"


def main():
    ativos = {
        "Ibovespa": "https://finance.yahoo.com/quote/%5EBVSP",
        "Dólar (USD/BRL)": "https://finance.yahoo.com/quote/USDBRL=X",
        "S&P 500": "https://finance.yahoo.com/quote/%5EGSPC",
        "Bitcoin (BTC/USD)": "https://finance.yahoo.com/quote/BTC-USD"
    }

    resultados = []
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    resultados.append(f"📊 INDICADORES FINANCEIROS - {data_hora}")
    resultados.append("-" * 45)

    for nome, url in ativos.items():
        valor = obter_valor(url)
        resultados.append(f"{nome}: {valor}")

    with open("indicadores.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(resultados))

    print("Arquivo 'indicadores.txt' gerado com sucesso!")


if __name__ == "__main__":
    main()
