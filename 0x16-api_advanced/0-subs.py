#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""


from requests import get


def number_of_subscribers(subreddit):
    """get number of subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    h = {'User-Agent': 'Mozilla/5.0 \
            (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

    response = get(url, headers=h)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
