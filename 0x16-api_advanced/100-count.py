#!/usr/bin/python3
"""
100-count
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None, count_dict={}):
    """
    Recursively retrieve hot posts from a subreddit and count occurrences
    of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count occurs of.
        hot_list (list): List to store hot post titles.
        after (str): Identifier for the next page of results.
        count_dict (dict): Dictionary to store keyword counts

    Returns:
        dict: Dictionary containing keyword counts.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, hot_list,
                               after, count_dict)
        else:
            for title in hot_list:
                for word in word_list:
                    if title.lower().count(word.lower()) > 0:
                        count_dict[word.lower()] = count_dict.get(
                            word.lower(), 0) + \
                            title.lower().count(word.lower())
            sorted_counts = sorted(count_dict.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return count_dict
    else:
        return None
