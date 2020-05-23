# Vasallius
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:  multi_cliboard.pyw save <keyword> - Saves clipboard to keyword.
#         multi_cliboard.pyw <keyword> - Loads keyword to clipboard.
#         multi_cliboard.pyw list - Loads all keywords to clipboard.
#         multi_cliboard.pyw delete all - Delete all keywords in clipboard.
#         multi_cliboard.pyw delete <keyword> - Deletes keyword in clipboard.


import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')
listofkeywords = list(mcbShelf.keys())

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:

    if sys.argv[1].lower() == 'list':
        print(list((mcbShelf.keys())))
        # pyperclip.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1].lower() == 'delete all':
        for x in mcbShelf.keys():
            del mcbShelf[x]

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()
