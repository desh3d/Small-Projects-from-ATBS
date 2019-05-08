import csv, os

# CSV Tuto

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')
exampleFile  = open('example.csv')
exampleReader = csv.reader(exampleFile)  #this csv.reader can only be used once write it again to  use again
#exampleData = list(exampleReader)
#print(exampleData)
for row in exampleReader:
    print('Row #'+ str(exampleReader.line_num) + ' ' + str(row))

# csv Writer

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()

# Tab seperated values writer

csvFile = open('output2.tsv', 'w', newline='')
outputWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
outputWriter.writerow(['spam', 'quanchi', 'bacon'])
outputWriter.writerow(['Hello, world!', 'shinok', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
csvFile.close()
