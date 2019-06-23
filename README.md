# Python Twitter Bot

Code to easily make your own twitter bot.

## Getting Started
Before this module can work, create an app with your [Twitter Developer](https://developer.twitter.com) account.

Under `Keys and tokens` find the information needed to fill out these fields in `tokens.py`:
```python
MY_TOKENS = Tokens(consumer_key="?",
                   consumer_secret="?",
                   access_key="?",
                   access_secret="?")
```

Make sure you're using python 3, then run:
```bash
pip3 install -r requirements.txt
```

## Usage
To manually tweet text from the command line, use:
```bash
python py-twitter-bot.py tweet "Hello world"
```

To tweet indefinitely from a predefined file of tweets, use:
```bash
python py-twitter-bot.py run --tweets tweets.txt --order sequential --frequency 60
```
Edit `tweets.txt` with your own tweets for your bot to choose from.

