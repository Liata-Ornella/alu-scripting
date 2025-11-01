#!/usr/bin/python3
"""
1-top_ten.py
Prints the titles of the first 10 hot posts for a subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    if not subreddit or type(subreddit) is not str:
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux:api_advanced:v1.0 (by /u/yourusername)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
