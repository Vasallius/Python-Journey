# Vasallius

import os
import re

# Initialize variables
list_of_text_files = []
list_of_matched_words = []

# Get regex pattern from user
pattern = input("Regex pattern to be searched: ")
regexpattern = re.compile(pattern)

# Gets all the paths of .txt files
for filename in os.listdir(os.getcwd()):
    filepath = os.path.join(os.getcwd(), filename)
    if filepath.endswith('.txt',):
        list_of_text_files.append(filepath)

#Iterate over the paths and open
for x in list_of_text_files:
    fh = open(x)
    for line in fh.readlines():
        try:
            matchedword = re.findall(regexpattern,line)

        except AttributeError:
            pass
        #Add to list matched words
        for x in matchedword:
            list_of_matched_words.append(x)
        
print(list_of_matched_words)
