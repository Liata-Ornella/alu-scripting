#!/usr/bin/python3
"""Recursively count keyword occurrences in subreddit hot post titles."""

import requests


def count_words(subreddit, word_list, after=None, counter=None):
    """Count how many times each word in word_list appears in hot titles."""
    if counter is None:
        counter = {}

    if not subreddit or not isinstance(subreddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALUStudent:v1.0"}
    params = {"after": after, "limit": 100}

    r = requests.get(url, headers=headers,
                     params=params, allow_redirects=False)
    if r.status_code != 200:
        return

    data = r.json().get("data", {})
    children = data.get("children", [])

    for post in children:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            w = word.lower()
            counter[w] = counter.get(w, 0) + title.count(w)

    next_after = data.get("after")
    if next_after:
        return count_words(subreddit, word_list, next_after, counter)

    results = [(k, v) for k, v in counter.items() if v > 0]
    if not results:
        return

    for w, c in sorted(results, key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(w, c))

