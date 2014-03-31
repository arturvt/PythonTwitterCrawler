from twython import Twython
from util import geo_location

class TwitterRest:
    APP_KEY = '6S5z4JRsLlRCTxFQrEbtBA'
    APP_SECRET = 'QAFSQK18WaYX9c1PepZj46O0lRGyajfgTb1wJAdvW0'
    ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIpzQgAAAAAANXi%2B%2FJxCxPyWTdkajpOYWTZXIXo%3Daf4rT7RalBFNFS7OWWYuUVsJSO13Qeu8ivWRTOPBU'
    OAUTH_TOKEN = '1370188885-an8iXcloxa3VxYy6aVGxi4r8jiVlrLaJPubEpYK'
    OAUTH_TOKEN_SECRET = 'tDQuev1CvFpHDIDmP1XbWx9WRfzFbUosp6Fn4Enut8'

    # access function
    def __init__(self):
        # self.twitter = Twython(self.APP_KEY, access_token=self.ACCESS_TOKEN)
        self.twitter = Twython(self.APP_KEY, self.APP_SECRET, self.OAUTH_TOKEN, self.OAUTH_TOKEN_SECRET)
    
    def search(self, query):
        search_result = self.twitter.search(q=query.decode('utf-8'), count=200)
        tweets_result = search_result['statuses']
        return tweets_result
    
    def seachByLang(self, lg, qnt, query):
        search_result = self.twitter.search(q=query.decode('utf-8'), count=qnt, lang=lg)
        tweets_result = search_result['statuses']
        return tweets_result
    
    def seachByLangAndDate(self, language, date, qnt, query):
        search_result = self.twitter.search(q=query.decode('utf-8'), count=qnt, lang=language, until=date)
        tweets_result = search_result['statuses']
        return tweets_result
    
    def seachByLangA(self, language, date, qnt, query):
        search_result = self.twitter.search(q=query.decode('utf-8'), count=qnt, lang=language, until=date)
        tweets_result = search_result['statuses']
        return tweets_result
    
    def searchByGeo(self, local, distance, qnt, query):
        location, (lat, lon) = geo_location.getGeocode(local)
        print 'Local: %s - lat:%s - lon: %s' %(location, lat, lon)
        local_data = '%s,%s,%skm' %(lat, lon, distance)
        print local_data
        search_result = self.twitter.search(q=query, count=qnt, geocode=local_data)
        tweets_result = search_result['statuses']
        return tweets_result
    
    def getTimeLine(self):
        return self.twitter.get_home_timeline(count='100')
    
#    def twitterAuth(self):
     
        # about the geocode: -10.184444, -48.333611), 10000, "km"
        #search_pt = twitter.search(q='#HojeEmDia', count=10, lang='pt')
        #search_br = twitter.search(q='#HojeEmDia', count=10, geocode='-10.184444,-48.333611,3000km')
        
        # about the geocode: -10.184444, -48.333611), 10000, "km"
        #search_pt = twitter.search(q='#HojeEmDia', count=10, lang='pt', result_type='mixed')
        #search_br = twitter.search(q='#HojeEmDia', count=10, lang='pt')
    
    
        #tweets_pt = search_pt['statuses']
        #tweets_br = search_br['statuses']
    
        #for tweet in tweets_pt:
        #    print "From PT - @%s: %s" %(tweet['user']['name'], tweet['text'].encode('utf-8'))
        
        #for tweet in tweets_br:
        #    print "From PT - @%s: %s" %(tweet['user']['name'].encode('utf-8'),  tweet['text'].encode('utf-8'))


# About the API
""" Returns tweets that match a specified query.

    Documentation: https://dev.twitter.com/doc/get/search

    :param q: (required) The query you want to search Twitter for

    :param geocode: (optional) Returns tweets by users located within
                    a given radius of the given latitude/longitude.
                    The parameter value is specified by
                    "latitude,longitude,radius", where radius units
                    must be specified as either "mi" (miles) or
                    "km" (kilometers).
                    Example Values: 37.781157,-122.398720,1mi
    :param lang: (optional) Restricts tweets to the given language,
                 given by an ISO 639-1 code.
    :param locale: (optional) Specify the language of the query you
                   are sending. Only ``ja`` is currently effective.
    :param page: (optional) The page number (starting at 1) to return
                 Max ~1500 results
    :param result_type: (optional) Default ``mixed``
                        mixed: Include both popular and real time
                               results in the response.
                        recent: return only the most recent results in
                                the response
                        popular: return only the most popular results
                                 in the response.

    e.g x.search(q='jjndf', page='2')

    text = tweet['text'].encode('utf-8') 
    print ("@%s:%s" %(tweet['from_user'].encode('utf-8'),tweet['text'].encode('utf-8')))
    print ("Tweet from @%s Date: %s" %  (tweet['from_user'].encode('utf-8'),tweet['created_at']))
    print (tweet['text'].encode('utf-8'),"\n")
    twitter.search(q='python', result_type='popular')
    ACCESS_TOKEN = twitter.obtain_access_token()
    print ("Access token: "+ACCESS_TOKEN)
    """