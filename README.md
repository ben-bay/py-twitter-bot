# Python Twitter Bot

Code to easily make your own twitter bot.

## Getting Started
Before this can work, fill out these fields in `tokens.py`:
```python
CONSUMER_KEY    = "?"
CONSUMER_SECRET = "?"
ACCESS_KEY      = "?"
ACCESS_SECRET   = "?"
```

You'll also want to edit `tweets.txt` with your own tweets for your bot to choose from.

## Usage
To tweet indefinitely from a predefined file of tweets, use::
```bash
python py-twitter-bot.py run --file tweets.txt 
```

Make sure you're using python 3.
