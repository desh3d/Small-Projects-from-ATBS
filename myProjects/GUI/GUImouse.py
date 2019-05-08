import os, pyautogui, time

# some basic mouse GUI tutorial

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

pyautogui.PAUSE = 1.5    #paue 1.5 sec after every gui function
print(pyautogui.size())
width, height = pyautogui.size()
print(width, height)

# move mouse cursor poosition
'''for i in range(10):
      pyautogui.moveTo(100, 100, duration=0.25)
      pyautogui.moveTo(200, 100, duration=0.25)
      pyautogui.moveTo(200, 200, duration=0.25)
      pyautogui.moveTo(100, 200, duration=0.25)

# move mouse cursor relative to current position of cursor
for i in range(10):
      pyautogui.moveRel(100, 0, duration=0.25)
      pyautogui.moveRel(0, 100, duration=0.25)
      pyautogui.moveRel(-100, 0, duration=0.25)
      pyautogui.moveRel(0, -100, duration=0.25)

# get mouse position
for i in range(200):
    time.sleep(1)
    print(pyautogui.position())

# clicks and drag
pyautogui.click()
pyautogui.click(10, 5)
pyautogui.mouseDown()
pyautogui.mouseUp()

  # square spiral pattern

time.sleep(5)
pyautogui.click()    # click to put drawing program in focus
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)   # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2)   # move down
    pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2)  # move up'''


# scroll
time.sleep(5)
pyautogui.scroll(1000) # up scroll
pyautogui.scroll(-300)  # down scroll
