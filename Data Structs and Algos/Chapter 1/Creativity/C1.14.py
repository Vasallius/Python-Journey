'''
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
'''


def function(sequence):
    lst = []
    for number in sequence:
        for number2 in sequence:
            if number*number2 % 2 == 1:
                if ((number, number2, number*number2)) not in lst:
                    lst.append((number, number2, number*number2))
    print(lst) if len(lst) > 0 else print(
        'No pair of numbers in which the product is odd')


function([12, 2])
function([12, 2, 1, 2, 21, 21, 1, 31, 3])
