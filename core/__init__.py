from util.time_parser import DateHandler

from util.util import initialMessage, getProgramByChannelAndDate,\
    getHashTagsForEPGRow, getTweetsRelatedToProgram

current_date, current_hour = initialMessage()
#current_hour = '22:45:00'
#current_date = '21/11/2013'
print ' ---------------- '
# first looks for a program in current time
programToCheck =  getProgramByChannelAndDate("GLOBO", current_date, current_hour)
if programToCheck is None:
    print 'No events to show.'
else:    
    start_date, start_time, duration, operator_name, program_name = programToCheck[0], programToCheck[1], programToCheck[2], programToCheck[3], programToCheck[4]
    print 'Found: %s. Starts at %s - %s with duration of %s' %(programToCheck[4], programToCheck[0], programToCheck[1], programToCheck[2])
    
    #hashTagsList = getHashTagsForEPGRow(programToCheck)
    
    getTweetsRelatedToProgram(program_name, start_date, start_time, duration)
    
    #if tweets_list is None:
    #    print 'Nothing to show'
    #else:
    #    for tweet in tweets_list:
    #        date = DateHandler(tweet['created_at'])
    #        print  date.getDate(),'-',date.getTime(), ' - ',  tweet['user']['name'].encode('utf-8')+':', tweet['text'].encode('utf-8')
 

# them looks for the related tweeter_epg entity
# code here

# them search for related ashtags. Code already done.

# them use all hashtags + Channel Name to search. Using filters.
print ' ---------------- '
