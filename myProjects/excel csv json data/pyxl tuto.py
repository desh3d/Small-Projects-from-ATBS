import os, openpyxl,datetime

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')
wb = openpyxl.load_workbook('example2.xlsx')
print(type(wb))
print(wb.sheetnames) #OR print(wb.get_sheet_names())  
sheet = wb['Sheet1'] #OR sheet = (wb.get_sheet_by_name('Sheet1'))
print(sheet.title)
actSheet = wb.active #OR print(wb.get_active_sheet())
print(actSheet)
sheet['C1'].value = 'hello'    #assign value to C5

print(sheet['A1'].value)
cell = sheet['B1']

print('Cell ' + cell.coordinate + ' is ' + cell.value)

print(sheet.cell(row=3, column=2).value)
for i in range(1,4):
    print(i, sheet.cell(row=i, column=2).value)
#print(sheet.get_highest_row())
#print(sheet.get_highest_column())
for rowofCellObjs in sheet['B1':'C3']:
    for cellObj in rowofCellObjs:
        print(cellObj.coordinate, cellObj.value)
for cellobj in list(sheet.columns)[0]:
    print(cellobj.value)


''' GO THROUGH EACH ROW

exData = {}

for row in range(2,sheet.max_row):
    state = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value
    cens = sheet['A'+str(row)].value
    exData[cens]= pop

print(exData)'''

