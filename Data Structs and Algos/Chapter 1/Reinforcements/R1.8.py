'''
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index
−n≤k<0, what is the equivalent index j ≥0 such that s[j] references
the same element?
'''

s = 'jedidiah'
n = len(s)  # 7
k = len(s) + 1

for x in range(-n, 0):
    j = x + n
    print(s[x], s[j])
