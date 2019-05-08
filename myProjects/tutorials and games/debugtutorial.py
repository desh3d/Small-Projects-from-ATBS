
#debugging tutorial

'''def boxPrint(symbol, width, height):
       if len(symbol) != 1:
          raise Exception('Symbol must be a single character string.')
       if width <= 2:
          raise Exception('Width must be greater than 2.')
       if height <= 2:
        raise Exception('Height must be greater than 2.')
       print(symbol * width)
       for i in range(height - 2):
           print(symbol + (' ' * (width - 2)) + symbol)
       print(symbol * width)

for sym, w, h in (('**', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
         try:
           boxPrint(sym, w, h)
         except Exception as err:
            print('An exception happened: ' + str(err)) 

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}'''

import os

#os.chdir('C:\\Users\\dhira\\Desktop\\gakes')


import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial' + str(n))
    total = 1
    for i in range(1, n + 1):
     total *= i
     logging.debug('i is ' + str(i) + ', total is ' + str(total))
     logging.debug('End of factorial' + str(n))
        
print(factorial(5))
logging.debug('End of program')

