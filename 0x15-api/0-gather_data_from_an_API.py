#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


def fetch_employee_todo_progress(employee_id, baseUrl):
    try:
        # Fetch user data to get the employee's name
        usrUrl = baseUrl + "/" + str(employee_id)
        usr_data = requests.get(usrUrl).json()
        employee_name = usr_data['name']

        # Fetch todos for the employee
        todosUrl = usrUrl + "/todos"
        todos = requests.get(todosUrl).json()

        # Calculate the progress
        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo['completed'])

        # Display progress
        print('Employee {} is done with tasks({}/{}):'.format(
            employee_name, completed_tasks, total_tasks))

        # List completed task titles
        for todo in todos:
            if todo['completed']:
                print(f'\t{todo["title"]}')

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
        sys.exit(1)

    baseUrl = "https://jsonplaceholder.typicode.com/users"
    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id, baseUrl)
