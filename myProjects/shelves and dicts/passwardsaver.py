#!

import pyperclip
import sys
os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

"""passward format is like this = {'websitename[username1,passward1,username2,passward2,]}"""


myPasswards={'Google':['dhirajdeshpande1596@gmail.com','desHE3D1596$','dhairyashil3d@gmail.com','Googleplay ID: dhairyashil1596'],
             'Reddit':['dhairyashil96','desh1596'],
             'Steam':['dhairyashil96','desh1596 '],
             'Skype':['dhairyashil3d','desh1596'],
             'Unity':['desh3d','Desh1596'],
             'Cisco':['desh3d','Desh1596']}
if len(sys.argv) < 2:
    print('Use of this proram is like this(not less than two arguments, one for programfilename and one for websitenamename): python pw.py[websitename] - copy account passward')
    sys.exit()

website = sys.argv[1]
if website in myPasswards:
    pyperclip.copy(myPasswards[website][1])
    print('Username is ' + (myPasswards[website][0]))
    print('Passward for ' + website + ' has been copied to clipboard')
    print(pyperclip.paste())
else:
    print('No passward is stored for ' + website + ' site')
#print(pyperclip.paste())
