fname = input('Enter file name:')
fhand = open(fname)
email = dict()
most = 0


for line in fhand:
    if not line.startswith('From'):
        continue
    words = line.split()
    if len(words) > 2:
        email[words[1]] = email.get(words[1],0) + 1

for x in email:
    if int(email[x]) > most:
        most = email[x]


for y in email:
    if email[y] == most:
        c = y

print(c, most)
