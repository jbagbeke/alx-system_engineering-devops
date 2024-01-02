#!/usr/bin/python3
"""
    Uses REST API and returns infor about his/her TODO list progress
                                                                    """
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/{}/{}'

    res_one = requests.get(url.format('todos', sys.argv[1]))
    res_two = requests.get(url.format('users', sys.argv[1]))

    if res_one.status_code == 200 and res_two.status_code == 200:
        res_one = res_one.json()
        res_two = res_two.json()

        if res_one['completed'] is True:
            num = 1
        else:
            num = 0

        print('Employee {} is done with tasks({}/20):'.format(
                                                        res_two['name'],
                                                        num
                                                        ))

        if res_one['completed'] is True:
            print('\t{}'.format(res_one['title']))
