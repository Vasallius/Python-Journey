'''
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
'''


def function(sequence):
    for number in sequence:
        count = sequence.count(number)
        if count > 1:
            print('There are duplicates')
            break
        print('Sequence is distinct')
        break


function([1, 2, 3, 4])
