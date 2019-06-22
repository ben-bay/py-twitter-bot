
import sys

import tweepy


def get_api(tokens):
    try:
        auth = tweepy.OAuthHandler(tokens.CONSUMER_KEY, tokens.CONSUMER_SECRET)
        auth.set_access_token(tokens.ACCESS_KEY, tokens.ACCESS_SECRET)
        api = tweepy.API(auth)
        return api
    except tweepy.error.TweepError as e:
        print(f"\nError: Have you replaced the ?s in tokens.py?\nTraceback:\n{e}")
        raise
    except:
        print(f"Unexpected error: {sys.exc_info()[0]}")
        raise


def tweet(api, text):
    try:
        return api.update_status(text)
    except tweepy.error.TweepError as e:
        print(f"\nError: Have you replaced the ?s in tokens.py?\nTraceback:\n{e}")
        raise
    except:
        print(f"Unexpected error: {sys.exc_info()[0]}")
        raise

