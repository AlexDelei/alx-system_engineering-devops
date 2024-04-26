#!/usr/bin/python3
"""
Make an api call on the subreddit and return the number subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    how many subscribers have subscribed for a certain sub reddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url)
    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    return 0
