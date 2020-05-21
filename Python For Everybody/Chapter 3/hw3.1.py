h = input('Enter hours:')
r = input('Enter rate per hour:')
h = float(h)
r = float(r)

def computepay(h,r):
    if h > 40:
        excess = h - 40
        h = h - excess
        pay = h * r + excess * 1.5 * r
        return pay
p = computepay(h,r)

print ('Pay', p)
