fname = input('Enter file name:')
if len(fname) < 1:
    fhand = open('mbox-short.txt')
else: fhand = open(fname)
email = dict()
most = 0

for line in fhand:
    if not line.startswith('From'):
        continue
    words = line.split()
    if len(words) > 2:
        email[words[1]] = email.get(words[1],0) + 1

emlist=list()

for k,v in email.items():
    emlist.append((v,k))

emlist.sort(reverse=True)

print(emlist[0][1], emlist[0][0])
