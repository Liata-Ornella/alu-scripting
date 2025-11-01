#!/usr/bin/python3
"""
2-recurse.py
Recursively collects titles of all hot posts for a subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles for a subreddit."""
    if hot_list is None:
        hot_list = []

    if not subreddit or type(subreddit) is not str:
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:api_advanced:v1.0 (by /u/yourusername)"
    }
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))

        next_page = data.get("after")
        if next_page:
            # Recursively fetch next page
            return recurse(subreddit, hot_list, next_page)
        return hot_list
    except Exception:
        return None
