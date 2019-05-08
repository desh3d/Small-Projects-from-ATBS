import PyPDF2, os

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

pdf1File = open('meetingminutes.pdf', 'rb')  # Enter pdf name in directory
pdf2File = open('meetingminutes2.pdf', 'rb') # Second PDF
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)  # Function to read the file
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)  #
pdfWriter = PyPDF2.PdfFileWriter()           # Function to write the file, just a funct not order to write, ,( like a refrence to write something)
for pageNum in range(pdf1Reader.numPages):   # Loop through pages
         pageObj = pdf1Reader.getPage(pageNum) # assign oage as an object
         pdfWriter.addPage(pageObj)            #add that object to addPage func
for pageNum in range(pdf2Reader.numPages):
         pageObj = pdf2Reader.getPage(pageNum)
         pdfWriter.addPage(pageObj)
pdfOutputFile = open('combinedminutes.pdf', 'wb')  # create new pdf file
pdfWriter.write(pdfOutputFile)  # write to new pdf, everything in addPage
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
