'''
Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes
a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
'''

from random import randrange


def choice(data):
    index = randrange(0, len(data))
    return data[index]


x = 100
while x > 0:
    print(choice([1, 2, 31, 861, 81, 81, 81, 1, 84, 8, 1]))
    x -= 1
