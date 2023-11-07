#!/usr/bin/python3
"""
Api that queries the RedditAPI
"""
import requests


def number_of_subscribers(subreddit):
    """ Queries the reddit api and returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'briansAPI'}

    try:
        response = requests.get(url, headers, allow_redirects=False)
        # Check if the request was succesful, else exit with 0
        if response.status_code != 200:
            return 0
        # Extract the subscribers count from the response
        data = response.json()
        subs = data['data']['subscribers']
        return subs

    except ValueError:
        return 0
