# Image Site Downloader

'''
Description:
Write a program that goes to a photo-sharing site like Flickr or Imgur, 
searches for a category of photos, and then downloads all the resulting images. 
You could write a program that works with any photo site that has a search feature.
'''

import requests
import bs4
import os

keyword = input("Download images for: ")

# Downloads webpage assosciated with that search keyword
res = requests.get("https://imgur.com/search?q=" + keyword)
res.raise_for_status

# Create directory to store images
os.makedirs(keyword, exist_ok=True)

# Checks for src values of images tags
soup = bs4.BeautifulSoup(res.text, 'html.parser')
image_elements = soup.select('img[src]')
image_links = []

# Extracts all the links and puts them into a list
for image in range(len(image_elements)):
    image_links.append(f"https:{image_elements[image].get('src')}")

for link in image_links:
    res = requests.get(link)
    res.raise_for_status()

    # Open directory and write contents
    image_file = open(os.path.join(keyword, os.path.basename(link)),
                      'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
        image_file.close()
