import os,sys, webbrowser, bs4, requests, pyperclip

# am trying to get first 2 websites searched in google and ope newtabs for same
# howerver w=am getting a /url?q=  before the actual url, maybe am missing
#someting in the html selecter, i dont know what is wrong with this. 



#os.chdir('D:\\Dhairyashil\\Software\\Python\\MyPyLibirary')
if len(sys.argv)> 1:
    adress = ' '.join(sys.argv[1:])
else:
    adress = pyperclip.paste()

print('Googling.....')    
res = requests.get('https://www.google.com/search?q=' + adress)
print(type(res))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,features="lxml")
elems = soup.select('.r a')
#print(elems[i].get('href'))
numOpen = min(3,len(elems))
print((elems[0].get('href')[7:]))
for i in range(numOpen):
    print((elems[i].get('href')[7:]))
    #webbrowser.open(elems[i].get('href')[7:])




