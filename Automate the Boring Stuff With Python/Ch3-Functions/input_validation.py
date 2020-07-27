# Input Validation

print('Please enter an integer.')

while True:  # Loop until given an integer
    try:
        integer = int(input('> '))
        print('Thank you for entering an integer.')
        break
    except ValueError:  # Handle if user input is not an integer
        print('Error: please enter an integer')
