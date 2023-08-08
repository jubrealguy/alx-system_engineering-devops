#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the
number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'CustomUserAgent'}
    """a function that queries the Reddit API and returns the
    number of subscribers for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
