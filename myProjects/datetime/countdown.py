import subprocess, os, time

# Countdown, what elsse

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

for i in range(10):
    print(i)
    time.sleep(1)

subprocess.Popen(['C:\Program Files\VideoLAN\VLC\\vlc.exe','D:\Dhairyashil\Entertainment\Misc\English\\01 Mr. Blue Sky.mp3'])  # change this to your custom program requirement
