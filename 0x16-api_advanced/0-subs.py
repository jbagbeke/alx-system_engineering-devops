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

    user_agent = {'User-agent': 'AlxRedditQuery'}
    query_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(query_url, headers=user_agent)

    response_data = response.json()

    try:
        return response_data.get('data').get('subscribers')
    except Exception:
        return 0
