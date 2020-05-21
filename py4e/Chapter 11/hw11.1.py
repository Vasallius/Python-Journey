import re
totalsum = 0
fhand = open('regex_sum_469333.txt')

for line in fhand:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    if len(x) > 0:
        for y in x:
            y = int(y)
            totalsum += y

print(totalsum)
