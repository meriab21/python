import xlrd
from xlwt import Workbook
wb = Workbook()
loc = ('test.xlsx')
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
a = sheet.col_values(1)
print(a)
#write to file
file = open("text.txt", 'a+')
for i in a:
    file.write(i)

#reading excel file after writing 

