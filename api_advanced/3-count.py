#!/usr/bin/python3
"""
3-count.py
Recursively counts keyword occurrences in subreddit hot post titles.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count occurrences of words in hot post titles."""
    if counts is None:
        counts = {}

    if not subreddit or not isinstance(subreddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after, "limit": 100}

    res = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)
    if res.status_code != 200:
        return

    data = res.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0) + title.count(w)

    next_page = data.get("after")
    if next_page:
        return count_words(subreddit, word_list, next_page, counts)

    results = [(k, v) for k, v in counts.items() if v > 0]
    if not results:
        return

    for w, c in sorted(results, key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(w, c))
