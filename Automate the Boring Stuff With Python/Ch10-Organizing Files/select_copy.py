# Vasallius

import os
import shutil
from pathlib import Path


dir1 = Path(
    r'C:\Users\Joseph\Desktop\dump')  # Replace path with directory containing jpg and png files

total = 0

for root, dir, file in os.walk(dir1):

    for x in file:
        # Check if file is a picture (jpg,png)
        if ".jpg" in x or ".png" in x:
            total += 1
            imagepath = (f"{root}\\{x}")
            # Replace path with your directory
            shutil.copy(imagepath, r"E:\New folder (2)")

print(f'{total} files copied.')
