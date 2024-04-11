#!/usr/bin/python3
"""
Fetch All subreddit subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Get the no of subscribers"""
    try:
        headers = {'User-Agent': 'My-User-Agent'}
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        respo = requests.get(url, headers=headers, allow_redirects=False)
        data = respo.json()
        return data.get('data').get('subscribers')
    except Exception:
        return 0
