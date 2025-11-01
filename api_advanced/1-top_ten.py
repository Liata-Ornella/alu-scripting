#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a subreddit."""

import requests


def top_ten(subreddit):
    """Prints the first 10 hot post titles for a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALUStudent:v1.0"}
    params = {"limit": 10}

    r = requests.get(url, headers=headers,
                     params=params, allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return

    try:
        posts = r.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))

