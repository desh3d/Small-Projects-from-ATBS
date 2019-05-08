
# this program copies specified files from directry tree which match the pattern into a specified folder
# also this program can look in folder tree and retrive path and size as per one's need
import os,shutil,re

#create a regx to detect speficic extionsios
os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

myregx = re.compile(r'''^(.*?)          #beforepart anything
                    (\.)                #escape . caracter
                    ((txt)|(png))$      #extension
                    ''', re.VERBOSE)
# loop walk through foldertree looking for regex in filenames
filename1= []
subfolderlist1 = []
folderlist1 = []
filename2 = []
subfolderlist2 = []
folderlist2 = []


for folderdir, subfolderdir, fileNameList in os.walk('E:\\Dhairyashil Backup\\Courses'):
    
    for fileName in fileNameList:
        filename1.append(fileName)
    for subfoldername in subfolderdir:
        subfolderlist1.append(subfoldername)
    for foldername in folderdir:
        folderlist1.append(foldername)

for folderdir, subfolderdir, fileNameList in os.walk('D:\\Dhairyashil\\Education\\Courses'):
    
    for fileName in fileNameList:
        filename2.append(fileName)
    for subfoldername in subfolderdir:
        subfolderlist2.append(subfoldername)
    for foldername in folderdir:
        folderlist2.append(foldername)
        

#print(folderdir)

        
for i in subfolderlist2:
    if i not in subfolderlist1:
#        print(i)
        

        #filename = mo.group(1)
        #extension= mo.group(3)
        #file = filename+extension
        #absWrkingdir = folderdir+'\\'+ fileName     #get absolute path of those files
        #abspath =absWrkingdir                       # IF REQUIRED os.path.join(absWrkingdir, fileANY)
        #destination = 'C:\\Users\\dhira\\Desktop\\gakes\\copytoThis'
        #print('copied ' + file + ' from ' + os.path.dirname(abspath) + ' to ' + destination)
        #shutil.copy(abspath,destination)             #copy the files in a new folder
        
        #if os.path.getsize(abspath) > 100:     #to get big files only and their absolutepath print--  remove regex part to check for every file
            #print(abspath)
           # print(os.path.getsize(abspath))


