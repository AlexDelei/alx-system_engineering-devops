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
        if respo.status_code == 200:
            data = respo.json()
            return data.get('data').get('subscribers')
        else:
            return 0
    except Exception as e:
        return 0
