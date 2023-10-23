#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Imported modules
requests
load
sys
"""
from json import load
import requests
from sys import argv


if __name__ == "__main__":

    def request(resource, param=None):
        """
        Retrieve user data using API
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        key = param[0]
        value = param[1]

        if param:
            url += ('?' + key + '=' + value)

        # Make a request and convert to json format
        r = requests.get(url)
        r = r.json()
        return r

    # Query for needed data only.
    user = request('users', ('id', argv[1]))
    tasks = request('todos', ('userId', argv[1]))
    compl_tasks = [task for task in tasks if task['completed']]

    print('Employee {} is done with tasks({}/{}):'.format(user[0]['name'],
                                                          len(compl_tasks),
                                                          len(tasks)))

    for task in compl_tasks:
        print('\t {}'.format(task['title']))
