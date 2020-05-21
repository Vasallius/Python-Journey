fname = input('Enter file name:')

if len(fname) < 1:
    fhandle = open('mbox-short.txt')
else: fhandle = open(fname)

d = dict()
lst = list()
for line in fhandle:
    if not line.startswith('From'):
        continue
    line = line.rstrip()
    line = line.split()
    if len(line) > 2:
        x = line[5]
        x = x.split(':')
        y = x[0]
        d[y] = d.get(y, 0) + 1

for key,value in d.items():
    lst.append((key,value))
lst.sort()

for x,y in lst:
    print (x,y)
