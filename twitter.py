import tweepy
import time

auth = tweepy.OAuthHandler('0fKqB0qvAPhkcC69O4za5MTRe','gmCqYTdLLhRU0zxpClcCkfEoa49o7yT1bzyCeQUTfCQNwQen6Q')
auth.set_access_token('1189630006395314182-vr2N9bxGDc8YyXrWfTRoh9YApo7GIB','lsh7z34sJ2LK13nKzwdjUkppFbIftwZOPwtBwv0hOYvBv')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Data Science'
nrTweets = 5

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Retweeted')
        tweet.retweet()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
