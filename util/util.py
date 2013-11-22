from datetime import datetime
from twitter_rest import TwitterRest
from time_parser import DateHandler
from time_parser import fitTime
from db.database_access import DatabaseManager
from twitter.twitter_test import searchForTweetsByDateAndDuration
import re

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

    # first get the list of programs of the day
    # Returns in this order:  epg_event.startdate, epg_event.starttime, epg_event.durationtime, broadcaster.name, program.name, epg_event.descriptor
    listByChannel = dbHandler.filterEPGByChannelNameDateTime(channel_name, startDate)

    givenDateTime = '%s - %s' %(startDate, startTime)
    # search for a program in the given time
    for row in listByChannel:
        programDateTimeStarts = '%s - %s' %(row[0], row[1])
        # checks if there is some program in exactly current time.
        if fitTime(programDateTimeStarts, row[2], givenDateTime, 0):
            return row
    return

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
           
def getHashTagsForProgram(program_name):
    listOfHash = dbHandler.getHashTagsPerProgram(program_name)
    if listOfHash is None:
        print 'No hashtags found.'
        return
    else:
        chars = ['(', ')', ',', '\'', '?']
        listOfHash_formated = []
        for hash_name in listOfHash:
            hash_name = str(hash_name)
            hash_name = re.sub('[%s]' % ''.join(chars), '', hash_name)
            listOfHash_formated.append(hash_name)
            
        return listOfHash_formated

def getTweetsRelatedToProgram(program_name, start_date, start_time, duration_time):
    #gets the hashtags for given program
    hashTags_list = getHashTagsForProgram(program_name)
    
    for hash_name in hashTags_list:
        print 'Searching for: ', hash_name
        searchForTweetsByDateAndDuration(start_date, start_time, duration_time, hash_name, program_name)
    
    print 'Finished. Number of hashs: ', len(hashTags_list)
