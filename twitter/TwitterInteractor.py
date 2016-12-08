import tweepy
from twitter import config


class TwitterInteractor:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        self.auth.set_access_token(config.access_token, config.access_secret)
        self.api = tweepy.API(self.auth)

    def get_messages(self, amount):
        public_tweets = self.api.home_timeline(count=amount)
        return list(map(self.format_tweet, public_tweets))

    def send_message(self, message):
        self.api.update_status(message)

    @staticmethod
    def format_tweet(tweet):
        return '{} at {}\n{}'.format(tweet.author.name, tweet.created_at, tweet.text)