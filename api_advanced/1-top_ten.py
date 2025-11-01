#!/usr/bin/python3
"""
1-top_ten.py
Queries the Reddit API and prints the titles of the
first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Project-Agent/1.0"}
    params = {"limit": 10}

    try:
        res = requests.get(url, headers=headers,
                           params=params, allow_redirects=False, timeout=10)
        if res.status_code != 200:
            print(None)
            return

        posts = res.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
