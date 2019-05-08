import os, pyautogui, time

# Looking Busy, it nudges a little every ten seconds to seem am working
# Change as per your need to seem like you are working

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

while True:
    time.sleep(10)
    pyautogui.moveRel(-10,0)
    
