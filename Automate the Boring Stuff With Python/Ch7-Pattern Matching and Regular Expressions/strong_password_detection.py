# Vasallius

import re

password = input("Enter password: ")

capital_letters = re.compile(r'[A-Z]')
lowercase_letters = re.compile(r'[a-z]')
numbers = re.compile(r'[0-9]')

if re.search(capital_letters,password) != None:
    has_capital_letters = True
else:
    has_capital_letters = False

if re.search(lowercase_letters,password) != None:
    has_lowercase_letters = True
else:
    has_lowercase_letters = False

if re.search(numbers,password) != None:
    has_numbers = True
else:
    has_numbers = False

if len(password) < 8:
    print("Password must be at least 8 characters long.")

if has_capital_letters and has_lowercase_letters and has_numbers:
    print("Congrats! You have a strong password.")