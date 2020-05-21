fname = input('Enter file name: ')
fhandle = open(fname)

count = 0
total = 0
for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue


    colonpos = line.find(':')
    value = line[colonpos+1:]
    fvalue = float(value)

    count = count + 1
    total = total + fvalue
    average = total/count

print ('Average spam confidence: ' + str(average))
