# Vasallius

import os
from pathlib import Path

dir1 = Path(
    r'C:\Users\Joseph\Desktop')  # Replace path with directory containing jpg and png files
for root, dir, file in os.walk(dir1):

    for x in file:
        filesize = os.path.getsize(f"{root}\\{x}")
        # Check if filesize is over 100MB
        if filesize > 100*1024*1024:
            print(f"{root}\\{x}, filesize: {filesize/(1024*1024)} MB")
