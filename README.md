# Python Twitter Bot

Code to easily make your own twitter bot.

## Getting Started
Before this can work, create an app with your [Twitter Developer](https://developer.twitter.com) account.
Next, fill out these fields in `tokens.py`:
```python
CONSUMER_KEY    = "?"
CONSUMER_SECRET = "?"
ACCESS_KEY      = "?"
ACCESS_SECRET   = "?"
```


Make sure you're using python 3.

## Usage
To manually tweet text from the command line, use:
```bash
python py-twitter-bot.py tweet <text here>
```

To tweet indefinitely from a predefined file of tweets, use:
```bash
python py-twitter-bot.py run --tweets tweets.txt 
```
Edit `tweets.txt` with your own tweets for your bot to choose from.

