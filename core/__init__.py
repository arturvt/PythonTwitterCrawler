from util import util
from util.time_parser import DateHandler

current_date, current_hour = util.initialMessage()

print ' ---------------- '
# first looks for a program in current time

#programToCheck =  util.getProgramByChannelAndDate("Globo", current_date, current_hour)
#print 'Found: %s. Starts at %s - %s with duration of %s' %(programToCheck[6], programToCheck[2], programToCheck[3], programToCheck[4])
programToCheck = ['29/10/2013','01:05:00','01:35:00']
hashTagsList = util.getHashTagsForEPGRow(programToCheck)

for tweet in hashTagsList:
    date = DateHandler(tweet['created_at'])
    print  date.getDate(),'-',date.getTime(), ' - ',  tweet['user']['name'].encode('utf-8')+':', tweet['text'].encode('utf-8')
 

# them looks for the related tweeter_epg entity
# code here

# them search for related ashtags. Code already done.

# them use all hashtags + Channel Name to search. Using filters.
print ' ---------------- '
