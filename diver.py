"""
File: diver.py
Author: Declan Sullivan

This script will take the current Wikipedia page and choose the next link to
follow.
"""

import requests
import time
import random
from bs4 import BeautifulSoup

BASE_URL = "https://en.wikipedia.org"

def test_read():
    curr_link = "https://en.wikipedia.org/wiki/43rd_Chess_Olympiad"

    for i in range(15):
        request = requests.get(curr_link)
        soup = BeautifulSoup(request.text, 'html.parser')
        links = soup.find_all('a')
        poss_destinations = []

        title = soup.find('h1', {"id": "firstHeading"}).text
        print(title + " --- " + curr_link)

        for link in links:
            if valid_link(link):
                poss_destinations += [link]

        curr_link = BASE_URL + random.choice(poss_destinations).get('href')

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
