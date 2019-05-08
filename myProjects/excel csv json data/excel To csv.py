import csv, os, json, openpyxl

# this code scan a directry for all excel files, and converts each of them to a corresponding csv files represinting each sheet as a seperate
#csv file having name as:[mainFileName] [sheetName] [.csv]  USE IT WISELY


os.chdir('C:\\Users\\dhira\\Desktop\\mywork\\excelSpreadsheets')

#rowData = []
for xlFilename in os.listdir('C:\\Users\\dhira\\Desktop\\mywork\\excelSpreadsheets'):
    if not xlFilename.endswith('.xlsx'):     # It will go down the code only if file is csv ie condition is false, if its true it will retrun to start of the for loop
        continue
    print(' Getting data from ' + xlFilename)
    wb = openpyxl.load_workbook(xlFilename)
    sheets = wb.sheetnames
    print(sheets)
    for sheetname in sheets:
        outputFile = open(''.join(list(xlFilename)[:-5]) + ' ' + sheetname +'.csv', 'w', newline='')    # magic file extension name changer
        outputWriter = csv.writer(outputFile)
        sheet = wb[sheetname]
        print('Getting data from sheet ' + sheetname + ' in file '  + xlFilename)
        for rowNum in range(1,sheet.max_row+1):
            rowData = []
            for colNum in range(1,sheet.max_column+1):
                rowData.append(sheet.cell(row=rowNum, column=colNum).value)     # In case you want all the data from all sheets in one list create empy list rawData=[] at beginning
            outputWriter.writerow(rowData)
        outputFile.close()
