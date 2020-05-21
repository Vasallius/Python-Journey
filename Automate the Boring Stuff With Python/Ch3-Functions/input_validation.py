# Input Validation
print('enter an integer')

try:
    integer = int(input())
    print (integer)
except ValueError:
    print ('Error: please enter an integer')