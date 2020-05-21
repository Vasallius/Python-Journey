#commaCode |

import copy

print('What list do you wanna view?')
print('The following lists are: Sizes, Colors, and Prices.')

Sizes = ['small', 'medium', 'large', 'extra-large']
Colors = ['red', 'blue', 'green']
Prices = ['100 USD', '200USD']

#make input value refer to variable instead of a string


list = eval(input())

def enumerate(listName):

    for i in range(len(list)-1):
       print(list[i], ', ', end='')

    print('and ' ,end='')
    print(list[-1])


enumerate(list)





