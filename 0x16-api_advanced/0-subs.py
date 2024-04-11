#!/usr/bin/python3
"""
0-subs
"""
import json
import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""
    try:
        url = "https://www.reddit.com/r/{0}/about.json".format(subreddit)
        headers = {'User-Agent': 'by u/qasqot79'}
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.RequestException as e:
        return 0
