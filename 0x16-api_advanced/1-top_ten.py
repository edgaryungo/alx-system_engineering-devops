#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Top ten function"""
    # Set a custom User-Agent to avoid Too Many Requests errors
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    params = {
        'limit': 10
    }

    # Reddit API URL to get the top posts for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Check if the subreddit exists
            if 'error' in data:
                print('None')
            else:
                # Extract and print the titles of the top 10 posts
                for post in data['data']['children']:
                    print(post['data']['title'])
        else:
            # Handle invalid subreddit or other errors
            print('None')
    except requests.exceptions.RequestException:
        # Handle request exceptions, e.g., network issues
        print('None')

# Example usage:
# subreddit_name = 'learnpython'
# print(f'Top 10 hot posts in the subreddit "{subreddit_name}":')
# top_ten(subreddit_name)
