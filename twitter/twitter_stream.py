from twython import TwythonStreamer


class MyStreamer(TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
        # Want to disconnect after the first result?
        # self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data

APP_KEY = '6S5z4JRsLlRCTxFQrEbtBA'
APP_SECRET = 'QAFSQK18WaYX9c1PepZj46O0lRGyajfgTb1wJAdvW0'
ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIpzQgAAAAAANXi%2B%2FJxCxPyWTdkajpOYWTZXIXo%3Daf4rT7RalBFNFS7OWWYuUVsJSO13Qeu8ivWRTOPBU'
OAUTH_TOKEN = '1370188885-an8iXcloxa3VxYy6aVGxi4r8jiVlrLaJPubEpYK'
OAUTH_TOKEN_SECRET = 'tDQuev1CvFpHDIDmP1XbWx9WRfzFbUosp6Fn4Enut8'
# Requires Authentication as of Twitter API v1.1
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


stream.statuses.filter(track='twitter')
#stream.user()  # Read the authenticated users home timeline (what they see on Twitter) in real-time
#stream.site(follow='twitter')