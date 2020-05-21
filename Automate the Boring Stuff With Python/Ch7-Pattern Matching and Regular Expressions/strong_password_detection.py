# Vasallius

import re

password = input("Enter password: ")

capital_letters = re.compile(r'[A-Z]')
lowercase_letters = re.compile(r'[a-z]')
numbers = re.compile(r'[0-9]')

has_capital_letters = True if re.search(capital_letters,password) != None else False

has_lowercase_letters = True if re.search(lowercase_letters,password) != None else False

has_numbers = True if re.search(numbers,password) != None else False

if len(password) < 8:
    print("Password must be at least 8 characters long.")

if has_capital_letters and has_lowercase_letters and has_numbers:
    print("Congrats! You have a strong password.")
else: 
    print("Weak password. Consider revising.")