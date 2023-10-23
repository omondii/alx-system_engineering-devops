#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
Imported modules
requests
load
sys
"""
from json import dump, load
import requests
from sys import argv


if __name__ == '__main__':
    def request(resource, param=None):
        """
        Retrieve user data using API
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            key = param[0]
            value = param[1]
            url += ('?' + key + '=' + value)

        r = requests.get(url)
        r = r.json()
        return r

    files = {}
    filename = 'todo_all_employees.json'
    users = request('users')
    for user in users:
        user_id = user['id']
        files.update({user_id: []})
        user_tasks = request('todos', ('userId', str(user_id)))
        for task in user_tasks:
            files[user_id].append({'username': user['username'],
                                   'task': task['title'],
                                   'completed': task['completed']})

        with open(filename, mode='w') as f:
            dump(files, f)
