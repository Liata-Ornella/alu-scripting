#!/usr/bin/python3
"""
0-subs.py
Queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALU-Project-Agent/1.0"}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        if res.status_code != 200:
            return 0
        data = res.json().get("data", {})
        return data.get("subscribers", 0)
    except Exception:
        return 0
