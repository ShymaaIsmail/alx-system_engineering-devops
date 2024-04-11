#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""
    try:
        url = "https://www.reddit.com/r/{0}/about.json".format(subreddit)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
                   "AppleWebKit/537.36 (KHTML, like Gecko) " +
                   "Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.RequestException as e:
        return 0
