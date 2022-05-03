import xlsxwriter

wb = xlsxwriter.Workbook('hello.xlsx')
worksheet = wb.add_worksheet()

worksheet.write(1, 1, 'Green')
worksheet.write(2, 1, 'Blue')
worksheet.write(3, 1, 'white')
worksheet.write(4, 1, 'red')
worksheet.write(5, 1, 'whate ever')

wb.close()