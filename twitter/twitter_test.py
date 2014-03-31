from fileinput import filename
from time import localtime, strftime
from twitter_rest import TwitterRest
from util.time_parser import DateHandler, fitTime, getTwitterTime, \
    getWindowsTime
import os


twt = TwitterRest()
# tests the Rest Search api
    

def searchForTweetsByDateAndDuration(startDate, startTime, durationTime, query, program_name):
    print 'Looking for', startDate, ":",startTime, 'with duration:', durationTime, 'Query=', query
    tweets_result  = twt.seachByLang('pt', 2000, query)
    hash_tags = []
    rts = []
    filtered_tweets = []
    list_tweets = []
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
                list_tweets.append(line)
                words = tweet['text'].encode('utf-8').split() #split the sentence into individual words
                if 'RT' in words: #see if one of the words in the sentence is the word we want
                    rts.append(tweet)
                for word in words:    
                    if word.find('#') != -1:
                        hash_tags.append(word)
            
    recordListAtTXT(program_name, query, list_tweets)
    print ' -------------------------- '
    print 'Total Tweets:', len(filtered_tweets)
    print 'RTs qnt: %d'  %(len(rts))
    print 'Hashs qnt: %d'  %(len(hash_tags))
    print ' -------------------------- '
    # for hashs in hash_tags:
    #     print hashs        
    
def searchQuery(program_name, query):
    tweets_result  = twt.search(query)
    tweet_list = []
    for tweet in tweets_result:
        date = DateHandler(tweet['created_at'])
        creation_date = date.getDate()
        creation_time = date.getTime()
        line = "%s - %s - @%s: %s" %(creation_date, creation_time, tweet['user']['name'], tweet['text'].encode('utf-8')) 
        tweet_list.append(line)
    
    recordListAtTXT(program_name, query, tweet_list)
    
def recordListAtTXT(program_name, query, listTweets):
    folderName = "C:\\Users\\avt\\Dropbox\\Mestrado\\workspace\\TweetResults\\%s\\" %(program_name.decode('utf-8'))
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    currenttime = strftime("%Y-%m-%d-%H-%M-%S", localtime())
    filename = "%s\\%s_%s.txt" %(folderName, currenttime ,query)
    file_txt = open(filename, "w")
    print 'creating file: ', filename
    for line in listTweets:
        file_txt.writelines(line+'\n')
    file_txt.close()

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
searchForTweetsByDateAndDuration('10/1/2014', '08:30:00', '02:00:00', '#Encontro', 'Encontro com Fatima Bernardes')
searchForTweetsByDateAndDuration('10/1/2014', '08:30:00', '02:00:00', '#EncontroComFatimaBernardes', 'Encontro com Fatima Bernardes')
searchForTweetsByDateAndDuration('10/1/2014', '08:30:00', '02:00:00', '#FatimaBernardes', 'Encontro com Fatima Bernardes')
#searchQuery("EncontroComFatimaBernardes", "Encontro com Fatima Bernardes")
#searchForTweetsByDateAndDuration('12/12/2013', '21:45:00', '02:35:00', '#TheVoiceBrasil', 'The Voice Brasil')
#searchForTweetsByDateAndDuration('12/12/2013', '21:45:00', '02:35:00', '#VBR', 'The Voice Brasil')
#test01('31/10/2013', '22:30:00', '01:10:00', '#VBR')
#test01('30/10/2013', '21:50:00', '01:10:00', '#botecodoratinho')
#test01('31/10/2013', '21:50:00', '01:10:00', '#botecodoratinho')