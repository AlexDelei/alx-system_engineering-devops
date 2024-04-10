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
        "User-Agent": "linux:0x16.api.advance:v1.0.0 (by /u/alexdelei)"
    }
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 400:
        return 0
    data = r.json().get("data")
    return data.get("subscribers")
