# from config import getApi
# import os
# import sys
# import time

# api = getApi()




# def postTweet(update):
#     status = api.PostUpdate(update)
#     print(status)

# def postStatus(update, inReplyTo):
    
#     api.PostUpdate(update, in_reply_to_status_id=inReplyTo)


# def start():
#     postStatus("@CanYouHearMeBot Hello ?", "@CanYouHearMeBot")


# start()

from config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, ACCOUNT_ID, ACCOUNT_NAME
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import random

import json

class StdOutListener(StreamListener): 
    def on_data(self, data):
        clean_data = json.loads(data)
        tweetId = clean_data["id"]
        rand = random.randint(1,6)
        if(rand == 1):
            tweet = "Can you hear me ?"
        if(rand == 2):
            tweet = "Hello ?"
        if(rand == 3):
            tweet = "Hello ? Can you hear me ?"
        if(rand == 4):
            tweet = "Arnaud ? Are you there ?"
        if(rand == 5):
            tweet = "Hello Youma ?"
        if(rand == 6):
            tweet = "I can't here you ? :(("            
        respondToTweet(tweet, tweetId)


def setUpAuth():
    # authentication of consumer key and secret 
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET) 
    # authentication of access token and secret 
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET) 
    api = tweepy.API(auth) 
    return api, auth

def followStream():
    api, auth = setUpAuth()
    listener = StdOutListener()

    stream = Stream(auth, listener)
    stream.filter(track=[ACCOUNT_NAME]) #filter=[ACCOUNT_ID]
    # publishTweet(tweet)

def respondToTweet(tweet, tweetId):
    api, auth = setUpAuth()
    api.update_status(tweet, in_reply_to_status_id=tweetId, auto_populate_reply_metadata=True )

if __name__ == "__main__":
    followStream()