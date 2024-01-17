#!/usr/bin/python3
"""
    A function that queries the Reddit API and returns the # of subscribers
                                                                        """
import requests


def number_of_subscribers(subreddit):
    """
        Queries REDDIT API and returns # of subscribers with given subreddit
                                                                        """
    if not subreddit:
        return 0

    query_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(query_url, allow_redirects=False)

    if 300 <= response.status_code < 400 or response.status_code != 200:
        return 0

    response_data = response.json()

    return response_data['data']['subscribers']
