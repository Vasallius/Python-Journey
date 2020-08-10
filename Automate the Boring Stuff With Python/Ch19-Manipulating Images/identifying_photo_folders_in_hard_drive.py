# Identifying Photo Folders in Hard Drive

from PIL import Image
import os

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not filename.endswith('.jpg') or filename.endswith('.png'):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        try:
            img = Image.open(os.path.join(
                foldername, os.path.basename(filename)))
            width, height = img.size
        except:
            print(f'Cannot open {filename} at {foldername}')

        # Check if width & height are larger than 500.

        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.

    if numPhotoFiles > ((numNonPhotoFiles+numPhotoFiles)/2):
        print(foldername)
