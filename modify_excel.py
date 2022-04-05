from openpyxl import load_workbook

workbook = load_workbook(filename='test.xlsx')

sheet = workbook.active

sheet['B2'] = "Meron"

workbook.save(filename='test.xlsx')
