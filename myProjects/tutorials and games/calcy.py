# CALCULATOR SMALL

while True:
 print('Enter your operation followed by two numbers')
 x =input()
 a = int(input())
 b = int(input())
 if x=='+':
    x= a+b
    print (x)
 elif x== '-':
    x=a-b
    print(x)
 elif x== '*':
    x = a*b
    print(x)
 elif x== '/':
    x= a/b
    print(x)
 else:
    print('you idiot')
    break
