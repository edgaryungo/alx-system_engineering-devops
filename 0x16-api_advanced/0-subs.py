#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests errors
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    # Reddit API URL to get the subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the number of subscribers from the response
            subscribers = data['data']['subscribers']
            
            return subscribers
        else:
            # Handle invalid subreddit or other errors
            return 0
    except requests.exceptions.RequestException:
        # Handle request exceptions, e.g., network issues
        return 0

# Example usage:
# subreddit_name = 'learnpython'
# subscribers_count = number_of_subscribers(subreddit_name)
# print(f'The subreddit "{subreddit_name}" has {subscribers_count} subscribers.')
