#!/usr/bin/python3
"""a recursive function that queries the Reddit API
and returns a list containing the titles
of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """The function to implement the logic"""
    link = f"https://www.reddit.com/r/{subreddit}/hot.json"
    r = requests.get(link, headers={"User-Agent": "My-User-Agent"},
                     params={"after": after})
    if r.status_code >= 400:
        return None
    for i in r.json().get("data").get("children"):
        hot_list += [(i.get("data").get("title"))]
    if not r.json().get("data").get("after"):
        return hot_list
    return recurse(subreddit, hot_list,
                   after=r.json().get("data").get("after"))
