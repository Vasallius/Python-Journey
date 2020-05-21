# Vasallius

import re

regex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

thirtydaylist = [4, 6, 9, 11]


date = re.search(regex, input("Enter date: "))


def validate_date():
    day = int(date.group(1))
    month = int(date.group(2))
    year = int(date.group(3))

    if year % 4 == 0:
        is_leap_year = True
    else:
        is_leap_year = False
    if day not in range(1, 32):
        return "Not a valid day."
    if month not in range(1, 13):
        return "Not a valid month."
    if year not in range(1000, 2999):
        return "Not a valid year."
    if month in thirtydaylist and day == 31:
        return "Invalid date. This month only has 30 days"
    if month == 2 and is_leap_year == True and day > 29:
        return "Invalid date. February only has 29 days"
    if month == 2 and is_leap_year == False and day > 28:
        return "Invalid date. February only has 29 days"
    else:
        return "This is a valid date."


print(validate_date())
