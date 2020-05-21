import random

numberOfStreaks = 0 #initialize variable to keep track of streaks
masterList = []     #create an empty list

for experimentNumber in range(10000):

#Code that creates a list of 100 'heads' or 'tails' values.

    for i in range(100):
        masterList.append(random.randint(0,1)) #0 and 1 to mimic head or tail values
    print(masterList)                          #print list for confirmation
    for x in range(94): #Used 94, to prevent IndexError
        if masterList[x:x+6] == [1]*6 or masterList[x:x+6] == [0]*6:
           numberOfStreaks += 1     #add 1 to numberOfStreaks variable
           print('streak')
           break
    masterList = []                 #without this, masterList keeps on growing as new data is appended to it

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
