#!/usr/bin/python3
"""
100-count
"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "my-script/1.0"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get("data", {})
        children = data.get("children", [])

        for post in children:
            title = post["data"]["title"].lower()

            for word in word_list:
                word_lower = word.lower()

                if word_lower in title:
                    counts[word_lower] = counts.get(word_lower, 0) + title.count(word_lower)

        after = data.get("after")
        return count_words(subreddit, word_list, after, counts)
    else:
        if counts:
            print_results(counts)
        else:
            print("Nothing to show.")

def print_results(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        print(f"{word}: {count}")

if __name__ == '__main__':
    # Let's check if the user passed a subreddit and a list of keywords as arguments
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
