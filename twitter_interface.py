
import sys

import tweepy


def get_api(tokens):
    try:
        auth = tweepy.OAuthHandler(tokens.consumer_key, tokens.consumer_secret)
        auth.set_access_token(tokens.access_key, tokens.access_secret)
        api = tweepy.API(auth)
        return api
    except tweepy.error.TweepError as e:
        if e.api_code == 89:
            print(f"\nError: Have you replaced the ?s in tokens.py?\nTraceback:\n{e}")
        raise
    except:
        print(f"Unexpected error: {sys.exc_info()[0]}")
        raise


def tweet(api, text):
    try:
        return api.update_status(text)
    except tweepy.error.TweepError as e:
        if e.api_code == 89:
            print(f"\nError: Have you replaced the ?s in tokens.py?\nTraceback:\n{e}")
        raise
    except:
        print(f"Unexpected error: {sys.exc_info()[0]}")
        raise

