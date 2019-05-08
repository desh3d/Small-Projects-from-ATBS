 #! python3
   # readCensusExcel.py - Tabulates population and number of census tracts for
   # each county.


'''SAMPLE DATA CensusTract	State	County	POP2010
01001020100	AL	Autauga	1912
01001020200	AL	Autauga	2170
01001020300	AL	Autauga	3373'''



import os, openpyxl,datetime, pprint

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')
wb = openpyxl.load_workbook('example2.xlsx')
sheet = wb['Sheet1']


exData = {}

# Each row in the spreadsheet has data for one census tract.    (2, Last Number of row+1)
print('Reading rows.........')

for row in range(2,79):
    state = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value
    cens = sheet['A'+str(row)].value

    exData.setdefault(state,{})
    exData[state].setdefault(county,{'tracts':0,'pop':0})# replace 0 with []  and add append to get values instead of total items in data structure 
    exData[state][county]['tracts']+=1                   #.append(cens)      To return actual  pop value
    exData[state][county]['pop']+=int(pop)               #.append(pop)


# this can create a new .py or .txt file containing all of excel data in dictionary data structure
pprint.pprint(exData)


'''print('Writing Results.........')
resultFile = open('census20.py','w')
resultFile.write('allData= '+ pprint.pformat(exData))
resultFile.close()'''


print('Done')

