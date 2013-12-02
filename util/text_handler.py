import collections
import re

# receives a tweet. Returns the body, head, text
def extractFormattedTweet(tweet):
    tweet = tweet.rstrip()
    #tweet = tweet.replace('\n','')
    tweet_head = tweet[:tweet.index('@')]
    tweet_body = tweet[tweet.index('@'):]
    tweet_user = tweet_body[:tweet_body.index(':')]
    tweet_text = tweet_body[tweet_body.index(':'):]
    
    formattedTweet = collections.namedtuple("Formatted", ['head','body','user','text'])
    
    formattedResult = formattedTweet(tweet_head,tweet_body,tweet_user,tweet_text)
    return formattedResult

# Looks for characters repetitions, and remove them. Also check if the word is misspelled.
# Returns the fixed string and the words fixed.
def fixWords(text):
    matcher = re.compile(r'([a-z])\1*')
    words = []
    #print ('\n'.join(match.group() for match in matcher.finditer(text)))
    for match in matcher.finditer(text.lower()):
        if len(match.group()) > 2:
            if 'k' in match.group():
                text = text.replace(match.group(),'risos')
            else:
                text = text.replace(match.group(),match.group()[0])
            
            words.append(match.group())
    
    return (text, words)


'''
exemplo1 = 'Encontro, amoooooooooooooooo!!!!!! #EncontroFatima'
exemplo2 = 'Natiruts massa amuuuu muitoo tudo isso!'

fixWords(exemplo1)
fixWords(exemplo2)
'''
            
#tweet = '22/11/2013 - 10:51:57 - @futuro: coisa boa assistir #EncontroFatima amo d+'

#formatted = extractFormattedTweet(tweet)

#print formatted.head
#print formatted.body
#print formatted.user
#print formatted.text
