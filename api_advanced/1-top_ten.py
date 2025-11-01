#!/usr/bin/python3
"""
1-top_ten.py
Prints the titles of the first 10 hot posts for a subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit."""
    if not subreddit or type(subreddit) is not str:
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/ALUStudent)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])
    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
