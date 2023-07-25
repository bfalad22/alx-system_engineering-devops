#!/usr/bin/python3
""" Import request module """
import requests
from sys import argv

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Get employee details
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        employee_data = employee_response.json()
        employee_name = employee_data['name']

        # Get employee's TODO list
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])

        # Print the progress
        print(f'Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):')

        # Print completed task titles
        for todo in todos_data:
            if todo['completed']:
                print(f'\t {todo["title"]}')

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

