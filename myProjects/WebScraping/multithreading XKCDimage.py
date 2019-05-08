import os,sys, webbrowser, bs4, requests, pyperclip,threading

# this is just multithreading of normal image downloader, It is done to fully utilize your internet bandwidth ie simultaneously downloads by using multiple finger(14 fingers) to download
# running their own peice of code and downloading seperately in order
# understand multithreadinng

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')
print('Running.....')
url = 'http://xkcd.com/'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd

def downloadxkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page....    ' + url)
    res = requests.get(url+str(urlNumber))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,features="lxml")
     # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
         print('Could not find comic image.')
    else:
         comicUrl = comicElem[0].get('src')
         #        Download the image.
         print('Downloading image ........  '+ 'http:' + (comicUrl))
         res = requests.get('http:'+comicUrl)
         res.raise_for_status()
         #       Save the image to ./xkcd.
         imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
         for chunk in res.iter_content(100000):
           imageFile.write(chunk)
         imageFile.close()

downloadThreads = []
for i in range(0,140,10):      # its a bit complicated to understand, i goes form i=0,i=10,i=20,i=30,40 upto 140 in 14 iterations
    downloadThread = threading.Thread(target=downloadxkcd, args=(i,i+9))  # here statComic=0 endComic=9, in second iteration startComic=10 endComi=19, upto (140,149)
    downloadThreads.append(downloadThread)# it download 10 comic at a single iteration, while these are downloading, other will start downloading simultaneously, total 140 comics
    downloadThread.start()    # add zero range, to download 1400 comics simultaneously, hi-speed internet

    # wait for all threads to end
#for downloadthread in downloadThreads:
#    downloadThread.join()      # by my calculation it should download 140 images in total.
print('Done')




'''
while not url.endswith('#'):
    print('Downloading page....    '+ 'http:' + url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
     # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
         print('Could not find comic image.')
    else:
         comicUrl = comicElem[0].get('src')
         #        Download the image.
         print('Downloading image ........  '+ 'http:' + (comicUrl))
         res = requests.get('http:'+comicUrl)
         res.raise_for_status()
         #       Save the image to ./xkcd.
         imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
         for chunk in res.iter_content(100000):
           imageFile.write(chunk)
         imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
'''


        
