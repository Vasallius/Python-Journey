'''
Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
'''

import random


def shuffle(listofelements):
    length = len(listofelements)
    newlist = []
    indexes = []
    newlist = [x for x in listofelements]
    for x in listofelements:
        index = random.randint(0, length-1)
        while index in indexes:
            index = random.randint(0, length-1)
        indexes.append(index)
        newlist[index] = x
    print(listofelements)
    print(newlist)


shuffle([1, 2, 3, 4, 5, 6, 67, 8])
