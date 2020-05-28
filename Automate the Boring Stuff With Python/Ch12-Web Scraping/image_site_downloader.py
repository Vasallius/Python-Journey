# Vasallius

# Import necessary modules
import requests
import bs4
import os

# Ask user for search keyword
keyword = input("Download images for: ")
folder_name = input("Enter name of folder you want to download images in: ")

# Downloads url link
res = requests.get("https://imgur.com/search?q=" + keyword)
res.raise_for_status

# Create directory to store images
os.makedirs(folder_name, exist_ok=True)

# Checks for src values of images tags
soup = bs4.BeautifulSoup(res.text, 'html.parser')
image_elements = soup.select('img[src]')
image_links = []

# Extracts all the links and puts them into a list
for x in range(len(image_elements)):
    image_links.append(f"https:{image_elements[x].get('src')}")

for x in image_links:
    # Download each link
    res = requests.get(x)
    res.raise_for_status()

    # Open directory and write contents
    imageFile = open(os.path.join('images', os.path.basename(x)),
                     'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
        imageFile.close()
