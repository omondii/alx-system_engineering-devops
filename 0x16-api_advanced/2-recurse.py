#!/usr/bin/python3
""" Recurse it """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ A recurcive function to query Reddit API and rerturn a list
    of all hot articles """
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'briansAPI'}

    if after:
        url += '?after={}'.format(after)

    try:
        response = requests.get(url, headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                for post in data['data']['children']:
                    hot_list.append(post['data']['title'])
                if 'after' in data['data']:
                    return recurse(subreddit, hot_list, data['data']['after'])
                else:
                    return hot_list

    except ValueError:
        return o
