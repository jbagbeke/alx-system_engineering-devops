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

    try:
        query_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

        response = requests.get(query_url)


        if response.status_code == 200:
            response_data = response.json()
            return response_data['data']['subscribers']

        return 0
    except Exception:
        return 0
