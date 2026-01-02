from openpyxl import Workbook

wb = Workbook ()
ws = wb.active

ws.title = "Planilha Excel-Python"

ws['A1'] = "Nome"
ws['B1'] = "Cidade"

wb.save("Informacoes.xlsx")