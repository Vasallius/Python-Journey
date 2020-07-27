# Input Validation

print('Please enter an integer.')

while True:
    try:
        integer = int(input('> '))
        print('Thank you for entering an integer.')
        break
    except ValueError:
        print('Error: please enter an integer')
