"""
File: setup.py
Author: Declan Sullivan

This script simply uses the hidden API information and establishes a connection
to the Twitter account the bot is hosted on.
"""

import tweepy
from config import *

def connect_account():
    """Connects to Twitter account with API keys."""
    auth = tweepy.OAuthHandler(C_KEY, C_SEC)
    auth.set_access_token(A_KEY, A_SEC)
    api = tweepy.API(auth)
    return api
