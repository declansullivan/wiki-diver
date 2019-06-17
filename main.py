"""
File: main.py
Author: Declan Sullivan

This script will control the bot. It should setup the connection to the bot,
then pick the next link to traverse and create the new tweet, as well as save
the path taken.
"""

import setup
import diver

if __name__ == '__main__':
    # Establish connection to Twitter account.
    API = setup.connect_account()

    # Get information for next tweet, tweet it.
    title, url = diver.create_tweet(API)
    API.update_status(title + " - " + url)
    