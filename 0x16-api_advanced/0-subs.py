#!/usr/bin/python3
"""a function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0."""
import requests


def number_of_subscribers(subreddit):
    """The function to implement the logic"""
    try:
        link = f"https://www.reddit.com/r/{subreddit}/about.json"
        r = requests.get(link, headers={"User-Agent": "My-User-Agent"})
        return r.json().get("data").get("subscribers")
    except Exception:
        return (0)
