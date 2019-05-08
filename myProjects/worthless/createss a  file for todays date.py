import datetime
import time

for i in range(0,3):
    
    y = (datetime.datetime.now ()).strftime("%Y "+'%m '+'%d '+'%H '+ '%M'+'%S'+'%f ')
    file = open(str(y)+ '.txt','a')
    file.write(input('enter what you want for todays\'s file:'))
    time.sleep(4)
print(str(i)+'.txt')

