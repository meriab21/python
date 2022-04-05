from xlwt import Workbook

wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(1, 0, 'Hope')
sheet1.write(2, 0, 'Meron')
sheet1.write(3, 0, 'Adama')
sheet1.write(4, 0, 'Harar')
sheet1.write(5, 0, 'Dire Dawa')

wb.save('meron.xlsx')
