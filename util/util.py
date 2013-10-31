from datetime import datetime
from database_access import DatabaseManager
from twitter_rest import TwitterRest
from time_parser import DateHandler
from time_parser import fitTime

dbHandler = DatabaseManager()
now = datetime.now()

def initialMessage():
    current_date = '%s/%s/%s' %(now.day, now.month, now.year)
    current_hour = '%s:%s:%s' %(now.hour,now.minute, now.second)
    print ("Hello. App stating at: %s - %s" %(current_date, current_hour))
    return (current_date, current_hour)
 
# looks for a single program that fits all arguments
def getProgramByChannelAndDate(channel_name, startDate, startTime):
    print "Looking for a program at channel %s starting at %s - %s" %(channel_name, startDate, startTime)
    # first get the lsit of programs of the day
    listByChannel = dbHandler.filterEPGByChannelName(channel_name)
    
    givenDateTime = '%s - %s' %(startDate, startTime)
    # search for a program in the given time
    for row in listByChannel:
        programDateTimeStarts = '%s - %s' %(row[dbHandler.DATE_START], row[dbHandler.TIME_START])
        # checks if there is some program in exactly current time.
        if fitTime(programDateTimeStarts, row[dbHandler.DURATION], givenDateTime, 0):
            return row
    return "Did't found...."

def getHashTagsForEPGRow(epgRow):
    timeLineTweets = TwitterRest().getTimeLine()
    programDateTimeStarts = '%s - %s' %(epgRow[0], epgRow[1])
    print 'looking for tweets from %s with duration of %s in a interval of 30 minutes more and less.' %(programDateTimeStarts, epgRow[2])
    listOfHashs = []
    for tweet in timeLineTweets:
        date = DateHandler(tweet['created_at'])
        givenDateTime = '%s - %s' %(date.getDate(), date.getTime())
        if fitTime(programDateTimeStarts, epgRow[2], givenDateTime, 30):
            if '#' in  tweet['text'].encode('utf-8'):
                listOfHashs.append(tweet) 
           
    return listOfHashs
            