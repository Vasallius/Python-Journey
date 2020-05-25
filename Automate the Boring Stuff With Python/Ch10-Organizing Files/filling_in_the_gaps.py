# Vasallius

import os
import shutil
import re
from pathlib import Path

source_folder = Path(input("Please type directory: "))
prefix = input("Enter given prefix: ")

regexpattern = re.compile(fr'''
^({prefix}) #Capture letters before the number
(\d*) #Capture numbers 
(\.\w+)$ #Capture file extension
''', re.VERBOSE)


found = []

for root, dir, file in os.walk(source_folder):

    for filename in file:

        # Check files with numbering
        mo = re.match(regexpattern, filename)

        # Execute code is filename matches regexpattern
        if mo is not None:

            prefix = mo.group(1)
            number_length = int(len(mo.group(2)))
            extension = mo.group(3)
            found.append(mo.group(2))

for x in range(1, len(found)+1):
    zeroes = '0' * (number_length - len(str(x)))
    filename = (f"{source_folder}/{prefix}{zeroes}{x}{extension}")

    if os.path.exists(filename) == False:
        next_num = found[x-1]
        next_num_of_zeroes = '0' * (number_length - len(str(next_num)))
        next_filename = (str(source_folder) + '/' + prefix + str(next_num_of_zeroes)
                         + str(next_num) + extension)
        shutil.move(next_filename, filename)
