#!/usr/bin/python3
"""
Reddit API
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    return the number of subscribers
    """
    url = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
    headers = {
        "User-Agent": "Custom User Agent"
    }
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()["data"]["subscribers"]
        return data
    else:
        return 0
