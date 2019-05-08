import csv, os
# This thing just runs through a dir loking fo cs files takes data, removes the first line from data and write to a new file with 2 before the extension, magic renaming


os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

for csvFilename in os.listdir('C:\\Users\\dhira\\Desktop\\mywork'):
    if not csvFilename.endswith('.csv'):     # It will go down the code only if file is csv ie condition is false, if its true it will retrun to start of the for loop
        continue
    print('Removing header from ' + csvFilename + '......')

    file = open(csvFilename)
    reader = csv.reader(file)
    data = list(reader)
    #print(data)
    del data[0]
    #print(data)
    outputFile = open((''.join(list(csvFilename[:-4]))+ '2'+ '.csv'), 'w', newline='')  # Magic File name changer!!!!!!!!!!!
    print('Writing rest of data to ' + csvFilename + '2')
    outputWriter = csv.writer(outputFile)
    for row in data:
        outputWriter.writerow(row)
    outputFile.close()
