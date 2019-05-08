import os
from PIL import Image
from PIL import ImageColor

# adds logo to every image in file directory
# change it as per your requiremtn for future use, see PIL documentation for other codes, functions

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

files = os.listdir('C:\\Users\\dhira\\Desktop\\mywork')

logoImg = Image.open('github.png')
#image = Image.open('andromeda.jpg')
logowidth, logoheight = logoImg.size
print(logowidth, logoheight)
#print(width, height)
#image2 = image.resize((2000,1000))    #  remember keep arguments inside a touple!!!

for imgFilename in os.listdir('C:\\Users\\dhira\\Desktop\\mywork'):
    if not imgFilename.endswith('.jpg'):
           continue
    image = Image.open(imgFilename)
    width, height = image.size
    resizedImage = image.resize((width , height))
    resizedImage.paste(logoImg, (width-logowidth, height-logoheight))
    resizedImage.save('addedlogo '+ str(''.join(list(imgFilename)[:-4])) + ' ' + '.png')  # magic name extension changer
print('done')

# It will go down the code only if file is jpg ie condition is false, if its true it will retrun to start of the for loop'''
       
