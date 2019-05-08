#This Program changes american syle date filenames to european style date names
import os,sys,re,shutil

#os.chdir('C:\\Users\\dhira\\Desktop\\gakes\\dates')  #alwys change the directory to where files are located


#regex can be changed as per need
myregex = re.compile(r'''^(.*?)                   #anything
                    (0[1-9]|10|11|12)           #month
                    (-|\/)                      #seperator
                    (0[1-9]|[1-2][0-9]|30|31)   #day
                    (-|\/)                      #seperator
                    (\d{4})                     #years
                    (.*?)$                       #afterPart
                    ''', re.VERBOSE)       

for amerFilename in os.listdir('C:\\Users\\dhira\\Desktop\\mywork\\dates'):
    mo = myregex.search(amerFilename)

    if mo==None:
        continue
    beforePart = mo.group(1)
    month = mo.group(2)
    sep1 = mo.group(3)
    day = mo.group(4)
    sep2 = mo.group(5)
    year = mo.group(6)
    afterPart = mo.group(7)
    euroFilename = beforePart + day + sep1 + month + sep2 + year + afterPart
    abpath = os.path.abspath(amerFilename)
    renamepath =  os.path.dirname(abpath)+'\\'+euroFilename
    #shutil.move(abpath, renamepath)   # check before running

    print(' Filename changed from ' + amerFilename + ' to ' + euroFilename)    
