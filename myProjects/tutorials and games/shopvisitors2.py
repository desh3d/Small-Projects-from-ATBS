#SHOP VISITERS CODE

ShopVisiters = {'jon':'angry62', 'nilesh':9696,'andy':'fat1454', 'conan':'duche41', 'jimmy':'fake2564'}
proDucts = ['mangoes', 'bananas', 'coconuts', 'oranges', 'watermelons', 'pinapple']

while True:
 username = input('Enter username:')
 passward = input('Enter passward:')

 if username in ShopVisiters.keys() and passward == ShopVisiters[username]:
    print('Welcome ' + str(username))
    break
 else:
    print('Wrong passward or username, please try again')
    x = input('If you want to create an account enter Y:')
    if x =='Y':
        while True:
         b = input('please enter your username:')
         c = input('please enter your passward:')
         d = input('please re-enter your passward:')
         if c != d:
             print(' given passwards did not match, please try again')
             continue
         elif b in ShopVisiters.keys():
             print('username already exists, try a different one')
             continue
         else:
             print('thank you for registering, please login again')
             ShopVisiters[b]=c
             break
 continue
productname = input('Enter correct fruit name in plural:')

if productname in proDucts:
    print('Fruits available, please proceed')
else:
    print('Fruit out of stock')
    add =input('Enter Y if you want put order for given fruit:')
    if add == 'Y':
        proDucts.append(productname)
        print('available products are:',str(proDucts))
