import re
x = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d', re.I)
mo = x.search('My number is 415-555-4242.')
print('Phone number found:' + mo.group())
