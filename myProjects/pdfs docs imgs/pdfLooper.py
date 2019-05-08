# combinePdfs.py - Combines all the PDFs in the current working directory into a single PDF.
# also it can scan PDF text for each page in every pdf file in a directory
# do modifications according to your requirement eg change directry, output file name, add phEmil regex, cut out specific pages from pdf, reorder pages, etc,
# , create pdf having specific set of texts using extractText()
# do what you want, modify!!!!





import PyPDF2, os, re

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

myregx = re.compile(r'''^(.*?)          #beforepart anything
                    (\.)                #escape . caracter
                    ((pdf))$            #extension
                    ''', re.VERBOSE)
pdfWriter = PyPDF2.PdfFileWriter()

for folderdir, subfolderdir, fileNameList in os.walk('C:\\Users\\dhira\\Desktop\\mywork\\pdfs'):
    
    for fileName in fileNameList:
        mo = myregx.search(fileName)
        
        if mo==None:
         continue
        filename = mo.group(1)
        pdf1File = open(folderdir+'\\'+ fileName, 'rb')
        pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
        print(fileName)

        for pageNum in range(2, pdf1Reader.numPages):
            pageObj = pdf1Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
            #txtOnPage = pageObj.extractText()   #If you want to scan pdf text and use re search
            # ADD THE PHONE AND EMAIL REGEX CODE YOU MADE HERE TO DESIRED OUTPUT
            
            
            
#pdfOutputFile = open('stuff.pdf', 'wb')
#pdfWriter.write(pdfOutputFile)  Writes on stuff.pdf all thats in the PageObj
pdfOutputFile.close()
pdf1File.close()

