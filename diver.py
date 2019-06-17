"""
File: diver.py
Author: Declan Sullivan

This script will take the current Wikipedia page and choose the next link to
follow.
"""

import requests
import random
from config import *
from bs4 import BeautifulSoup

BASE_URL = "https://en.wikipedia.org"

def create_tweet(api):
    """
    This method pulls the most recent tweet from the account as the current
    starting point to dive into. It picks a random link from this page, finds 
    its title, then tweets that information.
    """
    # Get most recent link.
    recent_tweet = api.user_timeline('WikiDiver')[0].text.split('-')
    curr_link = recent_tweet[1][1:]

    # Pull information from related page.
    request = requests.get(curr_link)
    soup = BeautifulSoup(request.text, 'html.parser')
    links = soup.find_all('a')
    poss_destinations = []

    # Find all valid links to next pages.
    for link in links:
        if valid_link(link):
            poss_destinations += [link]

    # Get next link and find relating title.
    curr_link = BASE_URL + random.choice(poss_destinations).get('href')
    request = requests.get(curr_link)
    soup = BeautifulSoup(request.text, 'html.parser')
    title = soup.find('h1', {"id": "firstHeading"}).text

    # Return information to tweet.
    return (title, curr_link)

def valid_link(link):
    """
    This method checks to see if the given link could be a valid next step. The
    links we are looking for connect to another Wikipedia page and have a title.
    """
    # Look for links with attributes title and href.
    if len(link.attrs) != 2:
        return False

    # URL should use /wiki/ to head to next page, should not be a help page,
    # denoted with a colon in the URL.
    href = link.get('href')
    if href and href[0:6] == '/wiki/' and href.count(":") == 0:
        return True

    return False
