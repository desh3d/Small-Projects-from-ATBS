def collatz(number):
    if number%2==0:
        return number//2
    else:
        return (number*3 + 1)
    
try: 
 i = int(input('Enter a number:'))
 while i !=1 :
  collatz(i)
  i = collatz(i)
  print(i)
except :
    print('type an integer')
