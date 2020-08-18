'''
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
'''


def function(number):
    number = int(number)
    counter = 0
    while number > 2:
        number /= 2
        counter += 1
    print(f'Number of times: {counter}')


function(input('Enter number greater than 2:'))
