import re
import math

fname = ('mbox.txt')
fhand = open(fname)

nolines = 0
total = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]*)',line)
    if len(x) > 0:
        nolines += 1
        total = total + int(x[0])
        print(x)

y = int(total/nolines)

print(y)
