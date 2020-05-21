# © Vasallius

from builtins import list

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

length = []
# append string lengths to lengthlist
for list in tableData:
    for word in list:
        length.append(len(word))

longeststring = max(length)

# print out table in organized manner


def printTable(listoflists):
    for x in range(4):
        for y in range(3):
            print(tableData[y][x].rjust(longeststring), end='')
        print('')


printTable(tableData)
