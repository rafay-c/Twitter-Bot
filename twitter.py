import tweepy
import time

auth = tweepy.OAuthHandler(*,*)
auth.set_access_token(*,*)

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
