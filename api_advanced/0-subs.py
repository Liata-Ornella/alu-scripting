#!/usr/bin/python3
"""
0-subs.py
Queries Reddit API and returns number of subscribers for a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return total subscribers for a subreddit."""
    if not subreddit or type(subreddit) is not str:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:api_advanced:v1.0 (by /u/yourusername)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except Exception:
        return 0
