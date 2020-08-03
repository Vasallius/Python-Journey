# Regex Search

'''
Description: 
Write a program that opens all .txt files in a folder and searches for any line 
that matches a user-supplied regular expression. The results should be printed to the screen.
'''

import os
import re

list_of_text_files = []
list_of_matched_words = []


pattern = input("Regex pattern to be searched: ")
regexpattern = re.compile(pattern)

# Gets all the paths of .txt files
for filename in os.listdir(os.getcwd()):
    if filename.endswith('.txt',):
        list_of_text_files.append(filename)

# Iterate over the paths and open
for filename in list_of_text_files:
    with open(filename) as txt_file:
        for line in txt_file.readlines():
            try:
                matchedwords = re.findall(regexpattern, line)
            except AttributeError:
                pass
            # Add to list matched words
            for matched_word in matchedwords:
                list_of_matched_words.append(matched_word)

print(f'{len(list_of_matched_words)} matches found.\n{list_of_matched_words}')
