from geopy import geocoders
from geopy.point import Point

from pygeocoder import Geocoder

def geocode(cityName):
    g = geocoders.GoogleV3()
    place, (lat, lng) = g.geocode(cityName,exactly_one=True)  
    print ("%s: %.5f, %.5f" % (place, lat, lng))

def getGeocode(query):
    g = geocoders.GoogleV3()
    geocodes = g.geocode(query, exactly_one=False)
    for geocode in geocodes:
        return geocode #returns the first ocurrency
    

def complexGeocode(query):
    g = geocoders.GoogleV3()
    geocodes = g.geocode(query, exactly_one=False)
    for geocode in geocodes:
        location, (lat, lon) = geocode
        print ("%s: %.5f, %.5f" % (location.encode('utf-8'), lat, lon))

def detectCountry(lat,lng):
    #url_geo = "http://ws.geonames.org/countryCode?lat=%s&lng=%s" %(lat,lng)
    print "Detecting: ",lat,lng
    results = Geocoder.reverse_geocode(lat, lng)
    if "Brazil" == results:
        results = "Brasil"
    return results[0].country
    

# tests...
'''  
lat = -20.6215856
lng = -40.4540415
detectCountry(lat, lng)

try:
    complexGeocode("Brazil")
except Exception, e:
    raise e

try:
    complexGeocode("Rio de Janeiro, Brazil")
except Exception, e:
    raise e

try:
    complexGeocode("Recife - Pernambuco, Brazil")
except Exception, e:
    print e

try:
    complexGeocode("Belo Horizonte, Brazil")
except Exception, e:
    print e

try:
    complexGeocode("Sao Paulo - Sao Paulo, Brazil")
except Exception, e:
    print e
'''
