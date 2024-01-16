#!/usr/bin/python3
"""
1-top_ten
"""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "my-script/1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])

        if data:
            for post in data:
                print(post["data"]["title"])
        else:
            print("Subreddit has no hot posts.")
    else:
        print(None)

if __name__ == '__main__':
    # Let's check if the user passed a subreddit as an argument
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
