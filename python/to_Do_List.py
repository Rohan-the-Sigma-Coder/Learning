import openpyxl as xl
wb = xl.load_workbook('To do list.xlsx')
sheet = wb['Sheet1']
cell = sheet['b3']
print(cell.value)
