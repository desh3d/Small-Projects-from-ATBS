#guess the number game
import random
secretNumber = random.randint(1,10)  # assigns randomnuber

for guessTaken in range(1,9):
    guess=int(input('Enter the number am thinking, you have 8 chances:'))
    if guess > secretNumber:
               print('your number is too high')
    elif guess < secretNumber:
               print('your number is too low')
    elif guess== secretNumber:
              print('congrats you guessed the number in ' + str(guessTaken) + ' guesses')
              break
    else:
        print('enter a number you idiot')

if guess== secretNumber:
              print('congrats you guessed the number in ' + str(guessTaken) + ' guesses')
else:
              print('well try but secret number is ' + str(secretNumber))
