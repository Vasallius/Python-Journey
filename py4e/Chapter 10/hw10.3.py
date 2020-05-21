import string
import time

d = dict()
masterlst = list()
histo = list()
fname = input('Enter file name:')
total = 0
if len(fname) < 1 :
    fhand = open('words.txt')
else: fhand = open(fname)

for line in fhand:
    print(line)
    time.sleep(0.1)
    line = line.strip()
    line = line.split()
    print(line)
    time.sleep(0.1)
    for word in line:
        word = word.lower()
        word = word.translate(word.maketrans('','',string.punctuation))
        word = list(word)
        print(word)

        for char in word:
            masterlst.append(char)

for x in masterlst:
    d[x] = d.get(x,0)+1

for key,value in d.items():
    histo.append((key,value))

histo.sort()
print(histo, '\n')

for x in d:
    z = d[x]
    total = total + z

print ('LETTER FREQUENCY ANALYSIS' + '\n')
for x,y in histo:
    print(x, '|', y, '|',  round(y/total*100,2),'%')

print ('LETTER FREQUENCY ANALYSIS DONE' + '\n')
