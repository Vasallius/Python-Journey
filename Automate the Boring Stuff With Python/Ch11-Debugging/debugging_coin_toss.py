# Debugging Coin Toss

'''
Description:
Rewrite the code and find the bugs.
'''

import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()

toss = random.randint(0, 1)

if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input().lower()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
