fname = input('Enter file name: ')
fhand = open(fname)

count = 0

for line in fhand:
    if not line.startswith('From: '):
        continue
    line = line.rstrip()
    line = line.split()
    count += 1
    print(line[1])

print("There were", count, "lines in the file with From as the first word")
