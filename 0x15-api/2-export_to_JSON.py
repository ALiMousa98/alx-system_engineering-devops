#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees and exporting to JSON"""


import json
import requests
import sys


def fetch_employee_todo_progress(employee_id, baseUrl):
    try:
        # Fetch user data to get the employee's name
        usrUrl = baseUrl + "/" + str(employee_id)
        usr_data = requests.get(usrUrl).json()
        employee_id = usr_data['id']
        employee_name = usr_data['username']

        # Fetch todos for the employee
        todosUrl = usrUrl + "/todos"
        todos = requests.get(todosUrl).json()

        # Export to JSON
        json_filename = f"{employee_id}.json"
        data = {
            "USER_ID": [
                {
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": employee_name
                }
                for todo in todos
            ]
        }
        with open(json_filename, 'w') as json_file:
            json.dump(data, json_file)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo_progress_csv.py <employee_id>")
        sys.exit(1)

    baseUrl = "https://jsonplaceholder.typicode.com/users"
    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id, baseUrl)
