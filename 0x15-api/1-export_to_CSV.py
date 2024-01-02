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

    user_id = sys.argv[1]
    user_name = user_info.get('username')
    csv_list = []

    for task in response:
        task_stat = str(task.get('completed'))
        task_title = task.get('title')

        tmp_list = [user_id, user_name, task_stat, task_title]
        csv_list.append(tmp_list)

    with open('{}.csv'.format(user_id), 'w') as file:
        csv_write = csv.writer(file, quoting=csv.QUOTE_ALL)
        csv_write.writerows(csv_list)
