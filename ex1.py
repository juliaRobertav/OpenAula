from openpyxl import load_workbook
wb = load_workbook('C:/Users/sn1021328/Desktop/teste.xlsx')
plan = wb.active
plan['A1'] = 'Nº'
wb.save('C:/Users/sn1021328/Desktop/teste.xlsx')
