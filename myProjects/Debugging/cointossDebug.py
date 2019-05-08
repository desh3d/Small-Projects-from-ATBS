import random,logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    logging.debug('guess stored value after random right now is '+ str(toss))
    if guess == 'heads' and toss == 1:
      print('You got it!')
      break
    else:
      print('Nope! Guess again!')

    guesss = input()
    if guess == 'tails' and toss == 0:
       logging.debug('guess stored value after random right now is '+ str(toss))
       print('You got it!')
    else:
       logging.debug('guess stored value after random right now is '+ str(toss))
       print('Nope. You are really bad at this game.')
