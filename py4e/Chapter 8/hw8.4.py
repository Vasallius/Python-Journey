fname = input('Enter file name: ')
fhand = open(fname)

masterlist = []

for line in fhand:
    line = line.rstrip()
    line = line.split()
    for i in line:
        if i not in masterlist:
            masterlist.append(i)
masterlist.sort()
print(masterlist)
