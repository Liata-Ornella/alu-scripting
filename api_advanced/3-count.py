#!/usr/bin/python3
"""
3-count.py
Recursively counts keyword occurrences in subreddit hot post titles.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count keywords in the titles of hot posts."""
    if counts is None:
        counts = {}

    if not subreddit or type(subreddit) is not str:
        return

    # Reddit API endpoint
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:api_advanced:v1.0 (by /u/yourusername)"
    }
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        # Go through each title and count words
        for post in posts:
            title = post.get("data", {}).get("title", "").lower().split()
            for word in word_list:
                word_lower = word.lower()
                counts[word_lower] = counts.get(word_lower, 0) + title.count(word_lower)

        # Get next page
        next_page = data.get("after")
        if next_page:
            # Recursive call
            return count_words(subreddit, word_list, next_page, counts)

        # When done: sort and print results
        sorted_counts = sorted(
            [(k, v) for k, v in counts.items() if v > 0],
            key=lambda x: (-x[1], x[0])
        )

        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

    except Exception:
        return
