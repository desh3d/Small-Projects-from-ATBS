#this proram returns file sizes of all the files and folders in a directry tree
#use pprint for pretty display
import os
path = 'D:\Dhairyashil\Software\Python'
path2 = 'D:\Dhairyashil\Download\Based On A True Story (2017) [BluRay] [720p] [YTS.AM]\Based.On.A.True.Story.2017.720p.BluRay.x264-[YTS.AM].mp4'
path3 = 'E:\Dhairyashil Backup\GAMES'

sizelist = []
for filename in os.listdir(path3):
 sizelist.append(os.path.getsize(path3 + '\\' +str(filename)))
 # OR sizelist.append(os.path.getsize(os.path.join(path3, str(filename))))

print(sizelist)
print(len(os.listdir(path3)))
