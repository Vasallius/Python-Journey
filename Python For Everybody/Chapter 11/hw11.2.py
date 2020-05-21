import re

regexcommand = input('Enter a regular expression: ')

nolines = 0

fname = ('mbox.txt')
fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    x = re.findall(regexcommand,line)
    if len(x) > 0:
        nolines += 1
        print(x)
        
print(nolines)
