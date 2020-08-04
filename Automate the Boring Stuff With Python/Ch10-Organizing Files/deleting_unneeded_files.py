# Deleting the Unneeded Files

'''
Description:
Write a program that walks through a folder tree and searches for 
exceptionally large files or folders—say, ones that have a file size of more than 100MB. 
(Remember that to get a file’s size, you can use os.path.getsize() from the os module.) 
Print these files with their absolute path to the screen.
'''

import os

directory = input('Enter directory path to examine: ')
size_filter = int(input('Look for files greater than __MB: '))

for root, dir, filename in os.walk(directory):

    for document in filename:
        filesize = os.path.getsize(f"{root}\\{document}")
        # 1 MB = 1024 * 1024 bytes
        if filesize > size_filter * 1024 * 1024:
            print(f"{root}\\{document}, filesize: {round(filesize/(1024*1024))} MB")
