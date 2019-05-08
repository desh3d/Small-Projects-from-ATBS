# there are 3 variables in here all named 'eggs' the funny thing is first it
#first it runs spam() calls spam and prints 'spam local' next assignes global
#global variable eggs = global( does not print immediatly becz no print function is given
#then bacon() is run prints local variale eggs as 'bacon local' then calls spam() while being inside bacon()
#prints spam local then prints eggs again as bacon local, lastly print(eggs) is a global variable
# as defined in second line of code

def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

spam()
eggs = 'global'
bacon()
print(eggs)


#this shit modifies the global variable eggs and assignes it new value 'spam' so print eggs prints spam instead of global, also print is checked after spam() so it has been modified,
#so sequence matters
print('\n')

def spam():
    global eggs
    eggs = 'spam'
 
eggs = 'global'
print(eggs)
spam()
print(eggs)

#funcion inside a function
print('\n')

def  ham(eggs):
    eggs = 'fsafasf'
    print(eggs)
    eggs = 'fsa'
def spam():
    toasts = 465464654
    print(toasts)

ham(spam())

eggs = 456465
print(eggs)
