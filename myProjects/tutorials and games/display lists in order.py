wwesuperstars = ['john','rock','finn','randy','aj','daneial','baron','braun','xavier','kofi','big e','dean','seth','tripple h']
wwewomen = ['sasha','ronda','bayley','mandy','sonya','naiome','charolette','mickie','alexa','tamina','nia']
wwestars = wwesuperstars + wwewomen
test = [3]

def addand(listname):
    slicedlist=listname[:-1]
    for i in slicedlist:
     mystring=((i)+','+' ')
     print(mystring, end='')
     
    print('and '+ listname[-1])
    #addlast= mystring+'and'+ str(listname[-1])
    #listname.insert(-1,'and')
    #for i in (listname):
    #print((i)+','+' ', end='')
addand(wwewomen)

def listThing(words):
    if len(words)==1:
        return words[0]
    return '{}, and {}'.format(', '.join(words[:-1]), words[-1])
print(listThing(wwewomen))
