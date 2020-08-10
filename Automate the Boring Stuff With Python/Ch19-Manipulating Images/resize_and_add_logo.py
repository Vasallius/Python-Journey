# Resize and Add Logo

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logo.size

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.gif') or filename.lower().endswith('.gif')) \
       or filename == LOGO_FILENAME:
        continue  # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    # Image must be at least twice bigger than logo to look good
    if not width >= 2 * (logoWidth) and height >= 2 * (logoHeight):
        continue

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print(f'Resizing {filename}...')
        im = im.resize((width, height))

    # Add logo.
    print(f'Adding logo to {filename}')
    im.paste(logo, (width - logoWidth, height - logoHeight), logo)

    # Save changes.
    im.save(os.path.join('withLogo', filename))
