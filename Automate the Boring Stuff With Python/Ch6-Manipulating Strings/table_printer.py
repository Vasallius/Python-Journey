# Table Printer

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

length = []

# Append string lengths to length list
for list in table_data:
    for word in list:
        length.append(len(word))

longeststring = max(length)

# print out table in organized manner
def print_table(listoflists):
    for x in range(4): # Number of items in a list
        for y in range(3): # Number of lists
            print(table_data[y][x].rjust(longeststring), end='')
        print('')

print_table(table_data)
