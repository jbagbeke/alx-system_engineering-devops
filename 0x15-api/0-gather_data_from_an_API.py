#!/usr/bin/python3
"""
    Uses REST API and returns infor about his/her TODO list progress
                                                                    """
import csv
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/{1}/{0}'
    url_two = 'https://jsonplaceholder.typicode.com/users/{}'

    user_info = requests.get(url_two.format(sys.argv[1])).json()
    name = user_info.get('name')
    response = requests.get(url.format('todos', sys.argv[1])).json()

    done_titles = [res.get('title') for res in response
                   if res.get('completed') is True
                   ]

    print('Employee {} is done with tasks({}/{}):'.format(
                                                    name,
                                                    len(done_titles),
                                                    len(response)
                                                    ))
    for resp in done_titles:
        print('\t {}'.format(resp))
