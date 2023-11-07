#!/usr/bin/python3
"""
Query the RedditApi
"""
import requests


def top_ten(subreddit):
    """ Query the Reddit api and print the first 10 hot posts for subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'briansAPI'}

    try:
        response = requests.get(url, headers, allow_redirects=False)
        if response.status_code == 200:
            # Checks if there are posts in the response
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                # if posts: extract and print the titles of the first 10 posts
                for i, post in enumerate(data['data']['children']
                                         [:10], start=1):
                    print(post['data']['title'])
        else:
            print(None)
            return 0

    except ValueError:
        return 0
