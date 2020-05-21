import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = input('Enter count:')
position = input('Enter position:')

# Retrieve all of the anchor tags

for x in range (int(count)):
    tags = soup('a')
    newurl = tags[int(position)-1].get('href', None)
    print (newurl)
    url = newurl
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
