from openpyxl import Workbook

dados = [
    ("Ana", 8.5),
    ("Lucas", 9.0),
    ("Marcos", 7.8)
]

wb = Workbook()
ws = wb.active

ws.append(("Nome","Nota"))

for a in dados:
    ws.append(a)

wb.save("AlunosNotas.xlsx")