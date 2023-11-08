import requests

def print_keyword_counts(counts):
    # Sort the counts by keyword and count
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    # Print the sorted counts
    for keyword, count in sorted_counts:
        print(f'{keyword}: {count}')

def count_words(subreddit, word_list, after=None, counts=None):
    # Set a custom User-Agent to avoid Too Many Requests errors
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    # Initialize counts as a dictionary to store keyword counts
    if counts is None:
        counts = {}

    # Reddit API URL to get the hot posts for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

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

            # Extract and process the titles of posts
            for post in data['data']['children']:
                title = post['data']['title']
                words = [word.lower() for word in title.split()]

                for keyword in word_list:
                    keyword = keyword.lower()
                    if keyword in words:
                        counts[keyword] = counts.get(keyword, 0) + words.count(keyword)

            # Check if there's a 'next' page of results
            after = data['data']['after']
            if after:
                # Recursively call count_words with the updated 'after'
                return count_words(subreddit, word_list, after, counts)
            else:
                # No more pages, print the keyword counts
                print_keyword_counts(counts)
        else:
            # Handle invalid subreddit or other errors
            return None
    except requests.exceptions.RequestException as err:
        # Handle request exceptions, e.g., network issues
        return err



# Example usage:
# subreddit_name = 'learnpython'
# keywords = ['python', 'java', 'javascript']

# print(f'Keyword counts for subreddit "{subreddit_name}":')
# count_words(subreddit_name, keywords)
