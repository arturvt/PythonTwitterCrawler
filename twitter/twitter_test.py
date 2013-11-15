from twitter_rest import TwitterRest
from util.time_parser import DateHandler, fitTime



twt = TwitterRest()
# tests the Rest Search api
def test01(startDate, startTime, durationTime, query):
    
    tweets_result  = twt.seachByLangAndDate('pt','2013-11-2',  200, query)
    hash_tags = []
    rts = []
    filtered_tweets = []
    filename = "C:\\Users\\avt\\Dropbox\\Mestrado\\workspace\\TweetResults\\01_11_2013_%s.txt" %(query)
    file_txt = open(filename, "w")
    for tweet in tweets_result:
        date = DateHandler(tweet['created_at'])
        creation_date = date.getDate()
        creation_time = date.getTime()
        if (creation_date == startDate) :
            programDateTimeStarts = '%s - %s' %(startDate, startTime)
            givenDateTime = '%s - %s' %(creation_date, creation_time)
            # checks if there is some program in exactly current time.
            if fitTime(programDateTimeStarts, durationTime, givenDateTime, 45):
                filtered_tweets.append(tweet)
                line = "%s - %s - @%s: %s" %(creation_date, creation_time, tweet['user']['name'], tweet['text'].encode('utf-8')) 
                file_txt.writelines(line+'\n')
                print line
                words = tweet['text'].encode('utf-8').split() #split the sentence into individual words
                if 'RT' in words: #see if one of the words in the sentence is the word we want
                    rts.append(tweet)
                for word in words:    
                    if word.find('#') != -1:
                        hash_tags.append(word)
            
    file_txt.close()
    print ' -------------------------- '
    print 'Total Tweets:', len(filtered_tweets)
    print 'RTs qnt: %d'  %(len(rts))
    print 'Hashs qnt: %d'  %(len(hash_tags))
    print ' -------------------------- '
    for hashs in hash_tags:
        print hashs        


# tests the home timeline api
def test02():
    timeline_result = twt.getTimeLine()
    print 'qnt of tweets: %d' %(len(timeline_result))
    for tweet in timeline_result:
        date = DateHandler(tweet['created_at'])
        creation_date = date.getDate()
        creation_time = date.getTime()
        print '%s-%s - User:%s - Local: %s - Text: %s' %(creation_date, creation_time, tweet['user']['name'], tweet['user']['location'],  tweet['text'].encode('utf-8'))
        
def test03(query):
    tweets_result  = twt.search(query)
    filename = "C:\\Users\\avt\\Dropbox\\Mestrado\\workspace\\TweetResults\\31_10_2013_%s_nofilter.txt" %(query)
    file_txt = open(filename, "w")
    for tweet in tweets_result:
        date = DateHandler(tweet['created_at'])
        creation_date = date.getDate()
        creation_time = date.getTime()
        line = "%s - %s - @%s: %s" %(creation_date, creation_time, tweet['user']['name'], tweet['text'].encode('utf-8')) 
        file_txt.writelines(line+'\n')
        print line
    

print ' ----- beginning -----'

#test03('Programa do Jo')
test01('1/11/2013', '01:00:00', '01:10:00', '#ProgramaDoJo')
test01('1/11/2013', '01:00:00', '01:10:00', '#JoSoares')
#test01('31/10/2013', '22:30:00', '01:10:00', '#VBR')
#test01('30/10/2013', '21:50:00', '01:10:00', '#botecodoratinho')
#test01('31/10/2013', '21:50:00', '01:10:00', '#botecodoratinho')