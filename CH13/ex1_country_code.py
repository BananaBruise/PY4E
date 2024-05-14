import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Important: As of January, 2024 this course no longer includes
# The use of Google's Geocoding API in the content.   This
# has been replaced by OpenStreetMap data
# See the file opengeo.py

# This file is here for previous versions of the course
# materials and since it uses a proxy server to access the API,
# it should work for a while.

print("See https://www.py4e.com/code3/opengeo.py")
serviceurl = 'http://py4e-data.dr-chuck.net/json'

api_key = 42

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + '?' + urllib.parse.urlencode(parms)
    print(url)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    country_code = None
    for comp in js['results'][0]['address_components']:
        if "country" in comp['types']:
            country_code = comp['short_name']

    if country_code != None: print('country code:', country_code)