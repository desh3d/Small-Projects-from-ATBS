import os
from PIL import Image
from PIL import ImageColor

# this module has to import like this itself,
# Tutorial and basic functions of pillow module

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

'''#       Colors
#print(ImageColor.getcolor('RED', 'RGBA'),ImageColor.getcolor('Black', 'RGBA'),ImageColor.getcolor('red', 'RGBA'))
#print(ImageColor.getcolor('chocolate', 'RGBA'),ImageColor.getcolor('Black', 'RGBA'))


catIm =  Image.open('andromeda.jpg')    # keep an andromeda image in same directory
#print(catIm.size)
#print(catIm.filename, catIm.format, catIm.format_description)


width, height = catIm.size
#print(width)
#print(height)
#catIm.save('mass effect.jpg')


#        New empty image
im = Image.new('RGBA', (100, 200), 'purple')   # rgba (100 pixels wide and 200 pixels tall) , backgroundColor)
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))  # nothing for background makes transperant(0,0,0,0)
im2.save('transparentImage.png')

#         crop

simplecroppedIm = catIm.crop((345, 345, 565, 560))  # rectangleTobeCropped co-ordinates( x Of topleft, y of Topleft, x of (bottomright + 1 to right), y of (bottomright + 1 to bottom))
simplecroppedIm.save('cropped.png')

#         copy to new img
catCopyIm = catIm.copy()

#           crop and paste
croppedIm = catIm.crop((335, 345, 565, 560))  # finding the exact co-ordinates of pixcels is up to you
print(croppedIm.size)
catCopyIm.paste(croppedIm, (0, 0))   # paste at topleft, ( the img is pasted starting at (0,0), its center is at bottomright from (0,0)
catCopyIm.paste(croppedIm, (0, 100))   # paste at as per your co-ordinates
catCopyIm.paste(croppedIm, (400, 500))  # paste at center maybe,
catCopyIm.save('pasted.png')

#         loop through all pixels from leftTop to rightBottom

catImWidth, catImHeight = catIm.size
croppedImWidth, croppedImHeight = croppedIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, croppedImWidth):
       for top in range(0, catImHeight, croppedImHeight):
            print(left, top)
            catCopyTwo.paste(croppedIm,(left, top))
catCopyTwo.save('tilesOfimage.png')


#            resize and rotate

width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 6), int(height / 6)))  # half size or reduce 6 times
quartersizedIm.save('quartersized.png')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('svelte.png')


catIm.rotate(90).save('rotated90.png')  # rotated 90 no problem, no black surface etc
catIm.rotate(180).save('rotated180.png')   #  rotated 90 no problem, no black surface etc
catIm.rotate(270).save('rotated270.png')  #  rotated 90 no problem, no black surface etc
catIm.rotate(6).save('rotated6.png')      # rotated 6 or any other degreem black surface cuts the image no problem, no black surface etc
catIm.rotate(6, expand=True).save('rotated6_expanded.png')  # custom rotate but img expands or shrinks to nothing cuts out of image

# mirror
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')


#    LOOPER         Put pixels and get pixels, generate colors in image using pixels

im = Image.new('RGBA', (100, 100))
im.getpixel((0, 0))
for x in range(100):
       for y in range(50):             # it will go someting like this, in first colum from top to bottom upto 50, thin second colum upto 50.....
            im.putpixel((x, y), (210, 210, 210))  # (position co-ords to apply color), (4 color value intensities)
for x in range(100):
       for y in range(50, 100):       # first colum from 50 to 100( y coordinates going down), and all 50 for each one x co-ordinate
             im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))  # assign color directly by using return value of getcolor
im.getpixel((0, 0))
im.getpixel((0, 50))
im.save('putPixel.png')'''



#  Drawing shapes on image


from PIL import Image, ImageDraw
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),fill='brown')
for i in range(100, 200, 10):
   draw.line([(i, 0), (200, i - 100)], fill='green')

im.save('drawing.png')


#  Drawing text and sizing text font

from PIL import ImageFont
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = 'FONT_FOLDER' # e.g. 'Library/Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
im.save('text.png')
