import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ('Enter url: ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
js = json.loads(data)

totalcomments = 0


for x in range (len(js['comments'])):
    for y in (js['comments'][x]):
        if y == 'count':
            totalcomments += int((js['comments'][x][y]))
print(totalcomments)
