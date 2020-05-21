fname = input('Enter file name:')
fhand = open(fname)
email = dict()

for line in fhand:
    if not line.startswith('From'):
        continue

    print(line)
    words = line.split()
    if len(words) > 2:
        email[words[1]] = email.get(words[1],0) + 1

print (email)

    
