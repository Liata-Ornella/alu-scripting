#!/usr/bin/python3
"""Recursively count keyword occurrences in subreddit hot post titles."""
import requests


def count_words(subreddit, word_list, after=None, counter=None):
    """Count how many times each word appears in hot titles."""
    if counter is None:
        counter = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:alu.api:v1.0"}
    params = {"after": after, "limit": 100}

    r = requests.get(url, headers=headers,
                     params=params, allow_redirects=False)

    if r.status_code != 200:
        return

    data = r.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for w in word_list:
            w = w.lower()
            counter[w] = counter.get(w, 0) + title.count(w)

    nxt = data.get("after")
    if nxt:
        return count_words(subreddit, word_list, nxt, counter)

    results = [(k, v) for k, v in counter.items() if v > 0]
    for w, c in sorted(results, key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(w, c))
