#idk where else to stick the resources I'm using for this
#https://pypi.org/project/gpxpy/
#https://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/HTTP.aspx

import requests
import json
import gpxpy

filename = open("09_27_20.gpx", 'r')
gpx = gpxpy.parse(filename)

lats = []
longs = []

for route in gpx.routes:
	for point in route.points:
		lats.append(float(point.latitude))
		longs.append(float(point.longitude))

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

addys = []

for l in lats:
	response = requests.get("https://geoservices.tamu.edu/Services/ReverseGeocoding/Webservice/v04_01/HTTP/default.aspx",
	apiKey = "eb6a7ee7e8ad43f69ea61d99c1b228daa", version = 410, lat = lats[l], lon = longs[l], format = "json")
	addys = response.json()['StreetAddresses']
	jprint(addys)

streetAddys = []

for a in addys:
    address = a['StreetAddress']
    streetAddys.append(address)

print(streetAddys)
