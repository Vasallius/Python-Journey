# Filling in the Gaps

'''
Description:
Write a program that finds all files with a given prefix, such as 
spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering 
(such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
Have the program rename all the later files to close this gap.
'''

import os
import shutil
import re


source_folder = input("Please type directory: ")
prefix = input("Enter given prefix: ")

regexpattern = re.compile(fr'''
^({prefix}) # Capture letters before the number
(\d*) # Capture numbers 
(\.\w+)$ # Capture file extension
''', re.VERBOSE)


found = []

for root, dir, filename in os.walk(source_folder):

    for document in filename:

        # Check files with numbering
        match_object = re.match(regexpattern, document)

        # Execute code is filename matches regexpattern
        if match_object is not None:

            prefix = match_object.group(1)
            number_length = int(len(match_object.group(2)))
            extension = match_object.group(3)
            found.append(match_object.group(2))

for x in range(1, len(found)+1):  # List of 1 up to number of files
    # len(001) - 1 = 2, so two zeroes before the number
    zeroes = '0' * (number_length - len(str(x)))
    # Supposed filename, if it exists
    supposed_filename = (f"{source_folder}/{prefix}{zeroes}{x}{extension}")

    # If filename doesn't exist
    if os.path.exists(supposed_filename) == False:
        # Get the next number in the found list
        next_num = found[x-1]
        next_num_of_zeroes = '0' * (number_length - len(str(next_num)))
        # Figure out the path of that file
        next_filename = (str(source_folder) + '/' + prefix + str(next_num_of_zeroes)
                         + str(next_num) + extension)
        # Move that file to the supposed filename, essentially renaming it in the process
        shutil.move(next_filename, supposed_filename)
