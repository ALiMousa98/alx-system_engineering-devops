#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees and exporting to JSON"""


import json
import requests
import sys


def fetch_employee_todo_progress(baseUrl):
    try:
        # Fetch user data to get the employee's name
        usr_data = requests.get(baseUrl + "/users").json()
        # Initialize data dictionary to store tasks for all employees
        data = {}

        for usr in usr_data:
            employee_id = usr['id']
            employee_name = usr['username']

        # Fetch todos for the employee
        todosUrl = baseUrl + "/todos"
        todos = requests.get(todosUrl).json()

        # store employee data to JSON
        data[employee_id] = [
                {
                    "username": employee_name,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                for todo in todos
            ]

        with open('todo_all_employees.json', 'w') as filename:
            json.dump(data, filename)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    
    baseUrl = "https://jsonplaceholder.typicode.com"
    fetch_employee_todo_progress(baseUrl)
