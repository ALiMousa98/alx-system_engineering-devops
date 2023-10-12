#!/usr/bin/python3
"""
Using reddit's API
"""


from requests import get
after = None


def recurse(subreddit, hot_list=[]):
    """get number of subscribers"""
    global after
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    h = {'User-Agent': 'Mozilla/5.0 \
            (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    params = {'after': after}

    results = get(url, headers=h, params=params, allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
