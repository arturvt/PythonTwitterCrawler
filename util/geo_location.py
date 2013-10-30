from geopy import geocoders

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

# tests...
'''
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
