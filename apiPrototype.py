#idk where else to stick the resources I'm using for this
#https://pypi.org/project/gpxpy/
#https://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/HTTP.aspx

import requests
import json
import gpxpy
from decimal import Decimal
from flask import jsonify

filename = open("09_27_20.gpx", 'r')
gpx = gpxpy.parse(filename)

lats = []
longs = []

for track in gpx.tracks:
	for segment in track.segments:
		for point in segment.points:
			lats.append(Decimal(point.latitude))
			longs.append(Decimal(point.longitude))


def jprint(obj):
    print(json.dumps(obj))

addys = []
#addys will hold the street addresses

i = 0

for l in lats:
	parameters = {
		"apiKey" : "eb6a7ee7e8ad43f69ea61d99c1b28daa",
		"version" : "4.10", 
		"lat" : lats[i],
		"lon" : longs[i],
		"format" : "json"
	}

	response = requests.get("https://geoservices.tamu.edu/Services/ReverseGeocoding/Webservice/v04_01/HTTP/default.aspx", params = parameters)
	addy = response.json()['StreetAddresses']
	#jprint(addy)
	addys.append(addy)
	i += 1

