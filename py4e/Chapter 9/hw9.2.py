fname = input('Enter file name:')
fhand = open(fname)
days = dict()

for line in fhand:
    if not line.startswith('From'):
        continue
    words = line.split()
    if len(words) > 2:
        days[words[2]] = days.get(words[2],0) + 1

print (days)
