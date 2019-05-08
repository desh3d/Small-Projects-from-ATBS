import subprocess, os

#subprocess Tuto, launch other applications

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
print(calcProc.poll())
print(calcProc.wait())
print(calcProc.poll())

#subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])

#subprocess.Popen(['C:\Program Files\VideoLAN\VLC\\vlc.exe','D:\\Dhairyashil\\Entertainment\\Movies\\Boogie.Nights.1997.1080p.BluRay.x264-[YTS.AM].mp4'])  # remember to put inside the list
#subprocess.Popen(['D:\\Dhairyashil\\Software\\Python\\python.exe','D:\\Dhairyashil\\Software\\Python\\datetimeTuto.py'])   # it runs in cmd not IDLE, so closes immediately,
#if pyscript takes sys.argv add a list containing args right after scriptName

subprocess.Popen(['start','hello.txt'], shell=True)   # launches default program set for the file, no need to define the path of program, START for windows
