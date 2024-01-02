#!/usr/bin/python3
"""
    Uses REST API and returns infor about his/her TODO list progress
                                                                    """
import csv
import json
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/{1}/{0}'
    url_two = 'https://jsonplaceholder.typicode.com/users/{}'

    # Creating neccessary dict structure for .json dump
    json_dict = {}

    for user_num in range(1, 11):
        user_info = requests.get(url_two.format(user_num)).json()
        response = requests.get(url.format('todos', user_num)).json()

        done_titles = [res.get('title') for res in response
                       if res.get('completed') is True
                       ]

        user_id = user_num
        user_name = user_info.get('username')

        # Creating neccessary dict structure for .json dump
        user_dict = {"{}".format(user_id): []}

        for task in response:
            task_stat = task.get('completed')
            task_title = task.get('title')

            # Creating neccessary json dict for saving
            tmp_dict = {
                    "username": "{}".format(user_name),
                    "task": "{}".format(task_title),
                    "completed": task_stat
                    }

            user_dict[str(user_id)].append(tmp_dict)

        json_dict.update(user_dict)


    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_dict, file)
