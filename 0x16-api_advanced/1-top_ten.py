#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""


from requests import get


def top_ten(subreddit):
    """get number of subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    h = {'User-Agent': 'Mozilla/5.0 \
            (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    params = {'limit': 10}

    response = get(url, headers=h, params=params)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        return 0
