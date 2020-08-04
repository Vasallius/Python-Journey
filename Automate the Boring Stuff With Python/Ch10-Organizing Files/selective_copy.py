# Selective Copy


'''
Description:
Write a program that walks through a folder tree and searches
for files with a certain file extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder.
'''

import os
import shutil

source_directory = input('Enter the absolute path of the source folder: ')
new_directory = input('Enter the absolute path of the destination folder: ')
extension = input('Enter what type of file you want to copy (e.g. jpg): ')

total_files = 0
for root, dir, filename in os.walk(source_directory):

    for document in filename:
        # Check if file is a picture (.jpg, .png)
        if document.endswith(extension):
            total_files += 1
            imagepath = (f"{root}\\{document}")
            shutil.copy(imagepath, new_directory)

print(f'{total_files} files copied to {new_directory}.')
