import xlrd

loc = ('test.xlsx')

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

print(sheet.col_values(2))
