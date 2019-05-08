
# this program copies specified files from directry tree which mathc the pattern into a specified folder
#create a regx to detect speficic extionsions
# keep it in python folder to work
import os,shutil,re
os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

myregx = re.compile(r'''^(.*?)          #beforepart anything
                    (\.)                #escape . caracter
                    ((txt)|(png))$      #extension
                    ''', re.VERBOSE)
# loop walk through foldertree looking for regex in filenames
for folderdir, subfolderdir, fileNameList in os.walk('C:\\Users\\dhira\\Desktop\\gakes'):
    
    for fileName in fileNameList:
        mo = myregx.search(fileName)

        if mo==None:
         continue

        filename = mo.group(1)
        extension= mo.group(3)
        file = filename+extension
        absWrkingdir = folderdir+'\\'+ fileName     #get absolute path of those files
        abspath =absWrkingdir                       # IF REQUIRED os.path.join(absWrkingdir, fileANY)
        destination = 'C:\\Users\\dhira\\Desktop\\gakes\\copytoThis'
        print('copied ' + file + ' from ' + os.path.dirname(abspath) + ' to ' + destination)
        #shutil.copy(abspath,destination)             #copy the files in a new folder
        



