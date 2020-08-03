# Extended Multi-Clipboard
# mcb.py - Saves and loads pieces of text to the clipboard.
# Usage:  multi_cliboard.py save <keyword> - Saves clipboard to keyword.
#         multi_cliboard.py <keyword> - Loads keyword to clipboard.
#         multi_cliboard.py list - Loads all keywords to clipboard.
#         multi_cliboard.py delete all - Delete all keywords in clipboard.
#         multi_cliboard.py delete <keyword> - Deletes keyword in clipboard.


import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')
listofkeywords = list(mcb_shelf.keys())

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]

elif len(sys.argv) == 2:

    if sys.argv[1].lower() == 'list':
        print(list((mcb_shelf.keys())))

    elif sys.argv[1].lower() == 'delete all':
        for x in mcb_shelf.keys():
            del mcb_shelf[x]

    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])


mcb_shelf.close()
