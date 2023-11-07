#!/usr/bin/python3
""" Recurse it """
import requests


def recurse(subreddit, hot_list=[], count=0, next_page=None):
    """ A recurcive function to query Reddit API and rerturn a list
    of all hot articles """
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'briansAPI'}

    if next_page:
        url += '?after={}'.format(next_page)

    try:
        response = requests.get(url, headers, allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json()['data']
        posts = data['children']
        for post in posts:
            count += 1
            hot_list.append(post['data']['title'])

        next_page = data['after']
        if next_page is not None:
            return recurse(subreddit, hot_list, count, next_page)
        else:
            return hot_list

    except ValueError:
        return o
