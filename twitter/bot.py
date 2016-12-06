import tweepy

from twitter import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.friends).items():
    print(status)