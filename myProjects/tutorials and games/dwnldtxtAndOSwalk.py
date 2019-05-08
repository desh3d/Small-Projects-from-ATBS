# store this in working directory to work properly and not get src not defined error
# this thing downloads a text file and displayes its last 250 characters
#tutorial
import os,sys,requests
#os.chdir('D:\\Dhairyashil\\Software\\Python')
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
print(res.status_code == requests.codes.ok)

'''for i,j,k in os.walk('D:\Dhairyashil\Software\Python'):
    for i in range(len(k)):
        sea = 'pg1112.txt'
        if sea in k[i]:
         print('found')'''
print(res.text[:250])
