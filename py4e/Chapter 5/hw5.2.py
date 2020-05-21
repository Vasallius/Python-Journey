
largest = None
integerlist = []


while True:
    try:
        number = input('Enter an integer number:')
        if number == 'done':
            break
        else :
            number = int(number)
            integerlist.append(number)
    except:
        print('Invalid input')
        continue

def getmin():
    smallest = None
    for i in integerlist:
        if smallest == None:
            smallest = i
        elif i < smallest:
            smallest = i
    return smallest

def getmax():
    largest = None
    for i in integerlist:
        if largest == None:
            largest = i
        elif i > largest:
            largest = i
    return largest
smallest = getmin()
largest = getmax()

print ('Maximum is', largest)
print ('Minimum is', smallest)
