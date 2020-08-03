# Mad Libs

'''
Description:
Create a Mad Libs program that reads in text files and
lets the user add their own text anywhere the word 
ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
'''

with open('template.txt', 'r') as template_file:
    string = template_file.read()

while True:
    while 'ADJECTIVE' in string:
        string = string.replace('ADJECTIVE', input('Enter an ADJECTIVE: '), 1)
    while 'NOUN' in string:
        string = string.replace('NOUN', input('Enter a NOUN: '), 1)
    while 'VERB' in string:
        string = string.replace('VERB', input('Enter a VERB: '), 1)
    break

with open('output.txt', 'w') as output_file:
    output_file.write(string)
