# Vasallius

'''This is the regex version of the strip() method'''

import re  # Import necesarry modules

samplelst = []

# Ask user for input
string_to_be_formatted = input("Enter string to be formatted: ")
character_to_be_removed = input(
    "Enter character to be stripped (pressing Enter removes whitespace left and right of string)")

# Here, we set regex pattern to capture the nonwhitespace part of the string and store it in trimmed_text variable
regex_pattern = re.compile(r'^(\s*)(.*)(\s*)$')
mo = re.search(regex_pattern, string_to_be_formatted)
trimmed_text = mo.group(2)

# Function that accepts two arguments, default second argument is whitespace symbol


def regex_strip(string_to_be_formatted, character_to_be_removed):
    # If user presses enter, strip whitespace left and right of text
    if (len(character_to_be_removed) < 1):
        print(f"Output: {trimmed_text}")
    # If user enters a symbol, strip that symbol from the string
    else:
        for char in string_to_be_formatted:
            samplelst.append(char)
        # Remove symbol from the list of characters
        while character_to_be_removed in samplelst:
            samplelst.remove(character_to_be_removed)
        # Join characters into a new list
        final_list = "".join(samplelst)
        print(f"Output:  {final_list}")


# Execute function
regex_strip(string_to_be_formatted, character_to_be_removed)
