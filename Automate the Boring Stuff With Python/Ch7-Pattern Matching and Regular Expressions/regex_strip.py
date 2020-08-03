# Regex Version of the strip() Method

'''
Description:
Write a function that takes a string and does the same thing as the strip() string method. 
If no other arguments are passed other than the string to strip, 
then whitespace characters will be removed from the beginning and end of the string. 
Otherwise, the characters specified in the second argument to the function will be removed from the string.
'''

import re

character_list = []

string_to_be_formatted = input("Enter string to be formatted: ")
character_to_be_removed = input(
    "Enter character to be stripped (pressing Enter removes whitespace left and right of string): ")

# (whitespace)(any)(whitespace)
regex_pattern = re.compile(r'^(\s*)(.*?)(\s*)$')
text = re.search(regex_pattern, string_to_be_formatted)
trimmed_text = text.group(2)


def regex_strip(string_to_be_formatted, character_to_be_removed):
    # If user presses enter, strip whitespace left and right of text
    if (len(character_to_be_removed) < 1):
        print(f"Output: {trimmed_text}")

    # If user enters a symbol, strip that symbol from the string
    else:
        for char in string_to_be_formatted:
            character_list.append(char)
        while character_to_be_removed in character_list:
            character_list.remove(character_to_be_removed)
        final_list = "".join(samplelst)
        print(f"Output:{final_list}")


regex_strip(string_to_be_formatted, character_to_be_removed)
