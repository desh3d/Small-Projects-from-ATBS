import os, pyautogui, time

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

# keyboard, screen GUI tutorial, simple guides. Modify as per your needs

'''# takes and returns screen pixels
im = pyautogui.screenshot()
print(im.getpixel((0, 0)))
print(im.getpixel((50, 200)))  # touple representing position   returns RGB touple value
print(pyautogui.pixelMatchesColor(50, 200, (130, 135, 144)))  # x,y, RGB   returns True or False


# image recognition

 # for understanding imagine face.png as a submit button image in a form filling website
 # its like magic, but really dumb one.
time.sleep(5)                # 5 secs to get to the required window and look for that exact img on the screen
print(list(pyautogui.locateAllOnScreen('face.png')))   # where face.png is a small part of atual screen where you want to look for this image *** returns   X(left),Y(top), width, height
print(pyautogui.locateOnScreen('submit.png'))   # input img must match exact(or rather take the part out by cropping the screenshot),
#print(pyautogui.center(( co_ordinate part of_ return_value of locateOnScreen FUNCTION )))   # this wil return exact center co-ordinates of mathced image and we can use it to click on
#pyautogui.click((678, 759))r




#  Keyboard GUI

pyautogui.click(100, 100)  # fro this keep a text box or txt file open ready at position
pyautogui.typewrite('Hello world! of j k Rawoling') # it clicks to get window ready an then types


##justin never got old  press alt+3 to double comment current line

pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])
pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')

pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')

#  OR  use HotKey instead

pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('shift', '5')

def commentAfterDelay():
    pyautogui.click(100, 100)
    pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
    time.sleep(2)
    pyautogui.hotkey('alt', '3')

commentAfterDelay()
