import os,sys, webbrowser, bs4, requests, pyperclip, pprint,re

#this program download all needed big images from a (given site)?, needs slight modifications for each site,
#not just that it also gets links to all next and previous pages and also displays their links, and if you want can also download images on those pages as well.
#it  can be similiar for any site, just some modifiacations

# changes to be made for each comic download
# Inster first page url in Baseurl===========
# Enter the folder name in Foldername  where you want to save the comic =========
# At the time started writing this code this was the only comic site i could think of which i had visited year ago!!!!!!!!
os.chdir('C:\\Users\\dhira\\Desktop\\gakes')

print('Downloading.....')
Baseurl = 'https://savitahd.net/savita-bhabhi-episode-88-p/'  # start url
Foldername = 'savita ep 88'
os.makedirs(Foldername , exist_ok=True)   # storage folder
for i in range(1):
    url = Baseurl
    print('Downloading base page......   ' + url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    #             Find the URL of the gif image.
    imglinks = soup.select("#gallery-2 > dl > dt > a")
    #pprint.pprint(imglinks)
    for i in range(len(imglinks)):
        imgurl = imglinks[i].get('href')  
        #imgurl = re.sub('.md','',gifurl)  #this returns the actual image url but with addition of .md before.gif
        if imglinks == []:
         print('Could not find comic image.')
        else:
         print('Downloading image.....    '+ imgurl)
         res = requests.get(imgurl)
         res.raise_for_status()
         imgFile = open(os.path.join(Foldername, os.path.basename(imgurl)),'wb')
         for chunk in res.iter_content(100000):
            imgFile.write(chunk)
         imgFile.close()
    nextlinks = soup.select('.page-links a')
    pprint.pprint(nextlinks)
    for j in range(len(nextlinks)):
     urlnow = nextlinks[j].get('href')
     #     Find the URL of the gif image.
     print('Downloading page......   ' + urlnow)
     res2 = requests.get(urlnow)
     res2.raise_for_status()
     soup = bs4.BeautifulSoup(res2.text, features="lxml")
     imglinks = soup.select(".entry-content img")
     #pprint.pprint(imglinks)
     for k in range(len(imglinks)):
        imgurl = imglinks[k].get('src')  
        imgurl = re.sub('.th|.md','',imgurl)  #this returns the actual image url but with addition of .md before.gif
        if imglinks == []:
         print('Could not find comic image.')
        else:
         print('Downloading image.....    '+ imgurl)
         res = requests.get(imgurl)
         res.raise_for_status()
         imgFile = open(os.path.join(Foldername, os.path.basename(imgurl)),'wb')
         for chunk in res.iter_content(100000):
            imgFile.write(chunk)
         imgFile.close()
print('Done')

 
