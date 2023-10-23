#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys

def get_employee_todo_list(employee_id):
    """ Script that uses JSONPlaceholder API to get information about employee """
    try:
        # Make a GET request to the API endpoint
        response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
        response.raise_for_status()

        todos = response.json()

        # Calculate the number of completed and total tasks
        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo['completed'])

        # Get the employee name (assuming user data is available)
        user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data['name']

        print(f'Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):')

        # Print the titles of completed tasks
        for todo in todos:
            if todo['completed']:
                print(f'\t{todo["title"]}')

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
