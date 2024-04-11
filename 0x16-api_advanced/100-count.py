#!/usr/bin/python3
"""a recursive function that queries the Reddit API
and returns a list containing the titles
of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, word, after=None):
    """The function to implement the logic"""
    try:
        # begin count at current page
        count = 0
        # link to api
        link = f"https://www.reddit.com/r/{subreddit}/hot.json"
        # request to api
        r = requests.get(link, headers={"User-Agent": "My-User-Agent"},
                         params={"after": after})
        if r.status_code != 200:
            return None
        # loop through each movie, get title and check if word exist
        # (case-insensitive)
        for i in r.json().get("data").get("children"):
            if word in (i["data"]["title"]).lower():
                count += 1
        # checks if this is the last page for hot articles
        if not r.json().get("data").get("after"):
            return count
        # recurse, start again and save to current count
        count += recurse(subreddit, word,
                         after=r.json().get("data").get("after"))
        # finally return final count
        return count
    except Exception:
        print(None)


def count_words(subreddit, word_list):
    """counts all keywords in list"""
    # checks if list is empty
    if not word_list:
        return None
    # sorts list alphabetically
    word_list = sorted(word_list)
    # get count of word
    count = recurse(subreddit, word_list[0].lower(), after=None)
    # check if count is 0 and prints if false
    if count != 0:
        print(f"{word_list[0]}: {count}")
    # recurse
    count_words(subreddit, word_list[1:])
