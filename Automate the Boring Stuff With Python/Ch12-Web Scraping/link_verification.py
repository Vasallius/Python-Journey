# Link Verification

import bs4
import requests

# Retrieve website
website_url = input('Enter website: ')
res = requests.get(website_url)
res.raise_for_status

# Get link elements
soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elements = soup.select('a[href]')

# Place all links in a list
links = []
for link in link_elements:
    links.append(link.get('href'))

print('Broken links: ')

for link in links:
    # Retrieve links
    try:
        if link.startswith('https://'):
            res = requests.get(link)
        else:
            res = requests.get("https:/" + link)
    except:
        pass

    # Check for 404 error
    if res.status_code == 200:
        pass
    elif res.status_code == 404:
        print(f"{link} returned a 404 error")
