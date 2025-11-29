from openpyxl import Workbook

dados = [
    {"Nome": "Ana", "Idade": 15, "Cidade": "SP"},
    {"Nome": "Bruno", "Idade": 16, "Cidade": "RJ"},
    {"Nome": "Carlos", "Idade": 14, "Cidade": "BH"}
]

wb = Workbook()
ws = wb.active
ws.title = "Alunos"

ws.append(["Nome", "Idade", "Cidade"])

#ADICIONAR AS LINHAS
for item in dados:
    ws.append([item["Nome"], item["Idade"], item["Cidade"]])

wb.save("Alunos.xlsx")

