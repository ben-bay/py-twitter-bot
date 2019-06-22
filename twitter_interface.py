
import sys

import tweepy

from tokens import *

try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
except tweepy.error.TweepError as e:
    print(f"\nError: Have you replaced the ?s in tokens.py?\nTraceback:\n{e}")
    raise
except:
    print(f"Unexpected error: {sys.exc_info()[0]}")
    raise


def tweet(text):
    try:
        return api.update_status(text)
    except tweepy.error.TweepError as e:
        print(f"\nError: Have you replaced the ?s in tokens.py?\nTraceback:\n{e}")
        raise
    except:
        print(f"Unexpected error: {sys.exc_info()[0]}")
        raise
