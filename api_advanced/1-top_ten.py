#!/usr/bin/python3
"""
1-top_ten.py
Queries the Reddit API and prints the titles of
the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    res = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return

    data = res.json().get("data")
    if not data or "children" not in data:
        print(None)
        return

    posts = data.get("children")
    for post in posts:
        title = post.get("data", {}).get("title")
        print(title)
