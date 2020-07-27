# Input Validation

print('Please enter an integer.')


def validate():
    while True:  # Loop until given an integer
        try:
            integer = int(input('> '))
            print('Thank you for entering an integer.')
            break  # Stop program when user enters an integer
        except ValueError:  # Handle if user input is not an integer
            print('Error: please enter an integer')


validate()  # Calls the define 'validate' function above
