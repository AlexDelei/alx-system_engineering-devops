#!/usr/bin/python3
"""
Fetch All subreddit subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Get the no of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    try:
        respo = requests.get(url, headers=headers, allow_redirects=False)
        data = respo.json()
        return data.get('data').get('subscribers')
    except Exception:
        return 0
