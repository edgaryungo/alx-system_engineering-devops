import requests

def recurse(subreddit, hot_list=None, after=None):
    # Set a custom User-Agent to avoid Too Many Requests errors
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    # Reddit API URL to get the hot posts for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    # If hot_list is None, initialize it as an empty list
    if hot_list is None:
        hot_list = []

    # Append 'after' to the URL if it's provided
    # if after:
    #     url += f'&after={after}'

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Check if the subreddit exists
            if 'error' in data:
                return None
            else:
                # Extract and append the titles of posts to hot_list
                for post in data['data']['children']:
                    hot_list.append(post['data']['title'])

                # Check if there's a 'next' page of results
                after = data['data']['after']
                if after:
                    # Recursively call recurse with the updated 'after'
                    return recurse(subreddit, hot_list, after)
                else:
                    # No more pages, return the hot_list
                    return hot_list
        else:
            # Handle invalid subreddit or other errors
            return None
    except requests.exceptions.RequestException:
        # Handle request exceptions, e.g., network issues
        return None

# Example usage:
# subreddit_name = 'learnpython'
# print(f'Titles of all hot articles in the subreddit "{subreddit_name}":')
# hot_articles = recurse(subreddit_name)

# if hot_articles is not None:
#     for i, title in enumerate(hot_articles):
#         print(f'{i + 1}. {title}')
# else:
#     print('Subreddit not found or an error occurred.')
