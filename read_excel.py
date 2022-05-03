import xlrd
import time
from xlwt import Workbook

# wb = Workbook()

# loc = ('test.xlsx')

# wb = xlrd.open_workbook(loc)

# sheet = wb.sheet_by_index(0)
# sheet.cell_value(0, 0)

# # a = sheet.col_values(1)

# # print(' '.join(a))

# total_rows = sheet.nrows
# # total_columns = sheet.ncols

# for i in range(0, total_rows):
#     print(sheet.cell_value(i, 1))
#     time.sleep(1.5)

wb = Workbook()
loc = ('exl_commnets.xlsx')
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
total_rows = sheet.nrows
for i in range(0, total_rows):
    print(sheet.cell_value(i, 0))
    time.sleep(1.5)
print()


