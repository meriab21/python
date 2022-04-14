from openpyxl import load_workbook

workbook = load_workbook(filename='test.xlsx')

sheet = workbook.active

sheet['C2'] = "55"
file = open("text.txt", 'r')
str = file.readline()
sheet['A2'] = str
# sheet['A3'] = "Brook"
# sheet['A4'] = "Doobale"
# sheet['A5'] = "Abebe"
# sheet['A6'] = "Kebede"
# sheet['B1'] = "Black panter"

workbook.save(filename='test.xlsx')
