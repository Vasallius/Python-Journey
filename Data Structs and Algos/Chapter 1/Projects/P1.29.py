'''
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
'''


import random

char = ['c', 'a', 't', 'd', 'o', 'g']

strings = []

while len(strings) < 720:
    random.shuffle(char)
    if ''.join(char) not in strings:
        strings.append(''.join(char))

print(strings)
