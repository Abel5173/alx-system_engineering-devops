#!/usr/bin/python3
"""
2-recurse
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    if not hot_list:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "my-script/1.0"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get("data", {})
        children = data.get("children", [])

        if children:
            hot_list.extend([post["data"]["title"] for post in children])

            # Recursively call with the next page's "after" parameter
            after = data.get("after")
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list if hot_list else None
    else:
        return None

if __name__ == '__main__':
    # Let's check if the user passed a subreddit as an argument
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
