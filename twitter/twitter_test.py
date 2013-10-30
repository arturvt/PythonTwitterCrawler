from twitter_rest import TwitterRest



twt = TwitterRest()
# tests the Rest Search api
def test01():

    tweets_result  = twt.seachByLang('pt', 2000, "#ProgramaDoJo")
    hash_tags = []
    rts = []
    #tweets_result = twt.searchByGeo("Brazil", "3000", 200, '#seeufossevoce')
    for tweet in tweets_result:
        print "Data: %s - @%s: %s" %(tweet['created_at'], tweet['user']['name'], tweet['text'].encode('utf-8'))
        words = tweet['text'].encode('utf-8').split() #split the sentence into individual words
        if 'RT' in words: #see if one of the words in the sentence is the word we want
            rts.append(tweet)
        for word in words:    
            if word.find('#') != -1 and not word in hash_tags:
                hash_tags.append(word)
            
    print ' -------------------------- '
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
        


print ' ----- beginning -----'
test02()