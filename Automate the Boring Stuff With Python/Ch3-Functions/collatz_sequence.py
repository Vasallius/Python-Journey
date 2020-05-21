#The Collatz Sequence
# credits to Jed

print('Input a number.')

def collatz(number): #function takes in user input number
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


number = int(input()) # inputted number is assigned to variable number
r = collatz(number)
print (r)

while r != 1:
    r = collatz(r)
    print (r)
print('congrats, you have solved the seuquence')


