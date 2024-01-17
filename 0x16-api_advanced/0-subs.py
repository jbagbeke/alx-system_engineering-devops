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
        user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
        
        query_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

        response = requests.get(query_url, headers=user_agent, allow_redirects=False)

        if 300 <= response.status_code < 400:
            return 0

        if response.status_code == 200:
            response_data = response.json()
            return response_data['data']['subscribers']

        return 0
    except Exception:
        return 0
