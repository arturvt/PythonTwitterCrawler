from twython import TwythonStreamer
from util.time_parser import DateHandler
from time import localtime, strftime
import os
from util import geo_location
   
class MyStreamer(TwythonStreamer):
    collected = []
    folderName = "C:\\Users\\avt\\Dropbox\\Mestrado\\workspace\\TweetResults\\Stream Tests\\"
    currenttime = strftime("%Y-%m-%d-%H-%M-%S", localtime())
    cntr = 0
    port = 0
    not_port = 0
    
    with_geo = 0
    with_place = 0
    
    geos = {}
    langs = {}
    def incrementGeos(self, value):
        if value not in self.geos:
            self.geos[value] = 0
            
        self.geos[value]+=1
        
    def incrementLang(self, value):
        if value not in self.langs:
            self.langs[value] = 0
            
        self.langs[value]+=1
    
    def setupFile(self, hashTag):
        self.hashtag = hashTag
        self.filename = "%s\\%s_%s.txt" %(self.folderName, self.currenttime ,self.hashtag)
        if not os.path.exists(self.folderName):
            os.makedirs(self.folderName)
        self.file_txt = open(self.filename, "w")
        print 'Created:',self.filename

    def getHashTag(self):
        return self.hashtag
    
    def on_success(self, data):
        try:
            if 'text' in data:
                date = DateHandler(data['created_at'])
                creation_date = date.getDate()
                creation_time = date.getTime()
                
                country = "No-Country"
                lang = "No-Lang"  
                
                if data['place'] is not None:
                    self.with_place += 1
                    country = data['place']['country']
     
                if data['geo'] is not None:
                    self.with_geo += 1
                    lat = data['geo']['coordinates'][0]
                    lng = data['geo']['coordinates'][1]
                    if country == "No-Country":
                        country = geo_location.detectCountry(lat,lng)
                
                if data['lang'] is not None:
                    lang = data['lang']
                    if lang == 'pt':
                        self.port+=1
                    else:
                        self.not_port+=1
    
                self.incrementGeos(country)
                self.incrementLang(lang)
                
                nolines = data['text'].encode('utf-8').splitlines()
                nolines = ' '.join(nolines)
                                
                line = "%s - %s - [%s] - (%s) - @%s: %s" %(creation_date, creation_time, country, lang , data['user']['name'], nolines.encode('utf-8'))
                
                print line
                
                self.file_txt.writelines(line+'\n')
                #print line
                self.cntr += 1
                self.collected.append(data['text'].encode('utf-8'))
                
                if self.cntr % 10 == 0:
                    print ' \n----------------------------------------------------------------------------------------  '
                    # counters for Brazilian Language
                    total = self.port + self.not_port
                    porcentagem_port = float(100*self.port) / float(total)
                    porcentagem_non_port = float(100*self.not_port) / float(total)
                    print 'Port', "{0:.0f}%".format(porcentagem_port), " - Non Port:", "{0:.0f}%".format(porcentagem_non_port)
                    print 'Port: %s  NotPort: %s ' %(self.port, self.not_port)
                    print self.langs
                    
                    print '********************'
                    # counters for place geo
                    porcentagem_place = float(100*self.with_place) / float(self.cntr)
                    porcentagem_geo = float(100*self.with_geo) / float(self.cntr)
                    print 'WithPlace', "{0:.0f}%".format(porcentagem_place), " - With geo:", "{0:.0f}%".format(porcentagem_geo)
                    print 'Place: %s  Geo: %s ' %(self.with_place, self.with_geo)

                    print self.geos
                
                    
                    print ' ----------------------------------------------------------------------------------------\n  '
                    

                #if len(self.collected) > 400:
                #    self.disconnect()
            # Want to disconnect after the first result?
            # self.disconnect()
        except:
            print 'Erro no encode. Data: ', len(data)

    def on_error(self, status_code, data):
        print status_code, data
    
    def getCollected(self):
        return self.collected
    
APP_KEY = '6S5z4JRsLlRCTxFQrEbtBA'
APP_SECRET = 'QAFSQK18WaYX9c1PepZj46O0lRGyajfgTb1wJAdvW0'
ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIpzQgAAAAAANXi%2B%2FJxCxPyWTdkajpOYWTZXIXo%3Daf4rT7RalBFNFS7OWWYuUVsJSO13Qeu8ivWRTOPBU'
OAUTH_TOKEN = '1370188885-an8iXcloxa3VxYy6aVGxi4r8jiVlrLaJPubEpYK'
OAUTH_TOKEN_SECRET = 'tDQuev1CvFpHDIDmP1XbWx9WRfzFbUosp6Fn4Enut8'
# Requires Authentication as of Twitter API v1.1
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stream.setupFile('BigBrother')
stream.statuses.filter(track='#BBB, #BigBrotherBrasil, #BigBrother, #BBB14')

#stream.user()  # Read the authenticated users home timeline (what they see on Twitter) in real-time
#stream.site(follow='twitter')