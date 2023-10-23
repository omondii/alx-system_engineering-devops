#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
Imported modules
requests
load
sys
"""
import csv
from json import load
import requests
from sys import argv


if __name__ == '__main__':
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

        r = requests.get(url)
        r = r.json()
        return r

    user = request('users', ('id', argv[1]))[0]
    tasks = request('todos', ('userId', argv[1]))

    # Export the data to .csv format
    csv_filename = argv[1] + '.csv'
    with open(csv_filename, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user['id'],
                             user['username'],
                             task['completed'],
                             task['title']])
