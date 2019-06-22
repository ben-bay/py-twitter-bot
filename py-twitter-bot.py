"""
TWITTER BOT
"""
import argparse
import sys
import os
import time

import reader
import twitter_interface


class Twitterbot():
    def __init__(self, tweets_filepath, order, frequency):
        self.tweet_n = 0
        self.tweets_filepath = tweets_filepath
        self.order = order
        self.frequency = frequency


    def chron_tweets(self):
        while True:
            self.tweet()
            self.sleep()


    def tweet(self, text=None):
        if text is None:
            if self.order == "random":
                text = reader.random_line(self.tweets_filepath)
            elif self.order == "sequential":
                text = reader.nth_line(self.tweets_filepath, self.tweet_n + 1)
        twitter_interface.tweet(text)
        self.tweet_n += 1


    def sleep(self):
        time.sleep(self.frequency * 60)


def process_args(args):
    """This function contains the logic for processing the argparser."""
    if args.which is "run":
        tweets_filepath = args.tweets
        if tweets_filepath is None or "":
            tweets_filepath = "tweets.txt"
        if not os.path.exists(tweets_filepath):
            raise ValueError(f"The path '{tweets_filepath}' does not exist.")

        twitterbot = Twitterbot(tweets_filepath, args.choose, int(args.frequency))
        return twitterbot.chron_tweets()

    elif args.which is "tweet":
        return twitter_interface.tweet(args.text)


def setup_argparse():
    parser = argparse.ArgumentParser(
        description="Description of the program here")
    subparsers = parser.add_subparsers(help='')

    run = subparsers.add_parser("run", help="Run your twitter bot process indefinitely.")
    run.set_defaults(which="run")
    run.add_argument('-t', '--tweets', action='store', type=str, default="tweets.txt",
                        help='Specify the filepath to tweets.txt.')
    run.add_argument('-c', '--choose', choices=["sequential","random"], default="random",
                        help="Options: 'sequential', 'random'")
    run.add_argument('-f', '--frequency', action="store", type=int, default=60,
                        help="Tweet frequency in minutes")

    tweet = subparsers.add_parser("tweet", help="Publish one tweet.")
    tweet.set_defaults(which="tweet")
    tweet.add_argument('text', nargs='+', action='store', type=str,
                        help='Text to tweet')
    return parser


def main():
    parser = setup_argparse()
    args = parser.parse_args()
    process_args(args)


if __name__ == "__main__":
    sys.exit(main())
