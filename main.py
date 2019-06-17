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
    API = setup.connect_account()

    diver.test_read()