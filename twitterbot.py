"""
TWITTER BOT
"""
import argparse
import sys
import os
import time

import reader
import twitter_interface

TWEET_NO = 0

def process_args(args):
    """This function contains the logic for processing the argparser."""
    if args.which is "run" or "tweet":
        tweets_filepath = args.path
        if tweets_filepath is None:
            tweets_filepath = "tweets.txt"
        if not os.path.exists(tweets_filepath):
            raise ValueError(f"The path '{tweets_filepath}' does not exist.")

        if args.choose is "random":
            tweet = reader.random_line(tweets_filepath)
        elif args.choose is "sequential":
            tweet = reader.nth_line(tweets_filepath, TWEET_NO + 1)

        if args.which is "tweet":
            return twitter_interface.tweet(tweet)

        if args.which is "run":
            while True:
                if args.choose is "random":
                    tweet = reader.random_line(tweets_filepath)
                elif args.choose is "sequential":
                    tweet = reader.nth_line(tweets_filepath, TWEET_NO + 1)
                twitter_interface.tweet(tweet)
                TWEET_NO += 1
                time.sleep(args.frequency * 60)
            pass


def setup_argparse():
    parser = argparse.ArgumentParser(
        description="Description of the program here")
    subparsers = parser.add_subparsers(help='')

    run = subparsers.add_parser("run", help="Run your twitter bot process indefinitely.")
    run.set_defaults(which="run")
    run.add_argument('-p', '--path', action='store', type=str, default=None,
                        help='Specify the filepath to tweets.txt.')
    run.add_argument('-c', '--choose', choices=["sequential","random"], default="random",
                        help="Options: 'sequential', 'random'")
    run.add_argument('-f', '--frequency', action="store", default=False,
                        help="Tweet frequency in minutes")

    tweet = subparsers.add_parser("tweet", help="Publish one tweet.")
    tweet.set_defaults(which="tweet")
    tweet.add_argument('-p', '--path', action='store', type=str, default=None,
                        help='Specify the filepath to tweets.txt.')
    tweet.add_argument('-c', '--choose', choices=["sequential","random"], default="random",
                        help="Options: 'sequential', 'random'")
    return parser


def main():
    parser = setup_argparse()
    args = parser.parse_args()
    process_args(args)


if __name__ == "__main__":
    sys.exit(main())
