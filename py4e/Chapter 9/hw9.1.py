afhandle = open('words.txt')

d = dict()
count = 0
for line in fhandle:
    line = line.rstrip()
    line = line.split()
    for x in line:
        count += 1
        d[x] = count
        print (d[x])

print (d)

lol = input('what value do you wanna see:')

print (d[lol])
