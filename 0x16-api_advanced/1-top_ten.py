#!/usr/bin/python3
"""
Query the top ten hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    the top ten queries
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User Agent'}
    try:
        respo = requests.get(url, headers=headers, allow_redirects=False)
        if respo.status_code == 200:
            data = respo.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        return None
    except Exception:
        return None
