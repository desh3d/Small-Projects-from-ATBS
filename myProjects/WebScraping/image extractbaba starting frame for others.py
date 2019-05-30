import os,sys, webbrowser, bs4, requests, pyperclip, pprint,re

# am trying to get first 2 websites searched in google and ope newtabs for same
# howerver w=am getting a /url?q=  before the actual url, maybe am missing
#someting in the html selecter, i dont know what is wrong with this. 

os.chdir('C:\\Users\\dhira\\Desktop\\gakes')
if len(sys.argv)> 1:
    adress = ' '.join(sys.argv[1:])
else:
    adress = pyperclip.paste()

print('Twitting.....')
url = 'https://www.sexbaba.net/Thread-bollywood-actresses-fake-nude-gif-images?page=33'              # starting url
os.makedirs('sexbaba', exist_ok=True)   # store comics in ./xkcd
while not url.endswith('#'):
    print('Downloading page......   ' + url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="lxml")
     #             Find the URL of the gif image.
    giflinks = soup.select(".post_body img")
    pprint.pprint(giflinks)
    for i in range(len(giflinks)):
        gifurl = giflinks[i].get('src')  #this returns the actual image url but with addition of .md before.gif
        gifurl = re.sub('.md','',gifurl)
        print('Downloading image.....    '+ gifurl)
        res = requests.get(gifurl)
        res.raise_for_status()
        gifFile = open(os.path.join('sexbaba', os.path.basename(gifurl)),'wb')
        for chunk in res.iter_content(100000):
            gifFile.write(chunk)
        gifFile.close()
    prevlink = soup.select('#content > div:nth-child(7) > div > a.pagination_previous')
    pprint.pprint(prevlink)
    url ='https://www.sexbaba.net/' + prevlink[0].get('href')
        
    #print(gifurl)
    #print(giflink)
    #if giflink == []:
    #     print('Could not find gif image.')
    #else:
    #     gifurl = giflink[0].get('src')
         #           Download the image.
     #    print('Downloading image ........  '+ (gifurl))
     #    res = requests.get(gifurl)
    res.raise_for_status()

    '''res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,features="lxml")
    elems = soup.select('twitter:image img')
print(elems)
print(elems[0].get('src'))
numOpen = min(3,len(elems))
#print((elems[0].get('href')[7:]))
for i in range(numOpen):
    print((elems[i].get('src')))
    #webbrowser.open(elems[i].get('href')[7:])'''




