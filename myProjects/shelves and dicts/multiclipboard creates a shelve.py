# This program creates dictionary of keys and corresponding text to copy, save or listall on the clipboard
# python3  not all programs can be run from python shell
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
   # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
   #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
   #        py.exe mcb.pyw list - Loads all keywords to clipboard.
   #create a bat file and store it in default path of windows to run this program via win+R


import shelve,pyperclip,pprint,sys
os.chdir('C:\\Users\\dhira\\Desktop\\mywork')
sh1 = shelve.open  ('myclip')
key1 = sys.argv[1].lower()
if len(sys.argv) < 1:
    print('Use of this proram is like this(not less than two arguments, one for programfilename and one for keyforCopyingtext): python http://pw.py  [websitename] - \
           copy corresponding text saved in shelve key')
elif key1 in sh1:
    pyperclip.copy(sh1[key1])
    print('copied text is ' + sh1[key1])
    print('Corresponding text for ' + key1 + ' has been copied to clipboard')
    print(pyperclip.paste())
elif key1=='list':
    print('keys available are ' + '\n' + '\n'.join(sh1.keys()))
    pyperclip.copy(' '.join(sh1.keys()))
elif key1 == 'save' :
    newvalue = pyperclip.paste()
    sh1.setdefault(sys.argv[2],newvalue)
elif key1=='del':
    del sh1[sys.argv[2].lower()]
    print( sys.argv[2] + ' deleted from shelve')
elif key1 == 'delete':
    for i in sh1.keys():
        del sh1[i]
else:
    print('No text is stored for ' + key1 + ' in the module')
    y =input('Do you want to add a new key to module(Y/N):')
    if y=='Y':
        sh1 = shelve.open  ('myclip')
        cpytxt = input('enter your copied text here:')
        sh1.setdefault(key1,cpytxt)
    else:
        sys.exit()
sh1.close()

 
 
