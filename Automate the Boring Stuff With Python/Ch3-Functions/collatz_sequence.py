# The Collatz Sequence

print('Input a number.')


def collatz(number):  # function takes in user input number
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


number = int(input())
result = collatz(number)
print(result)

while result != 1:  # Looping mechanism
    result = collatz(result)
    print(result)
