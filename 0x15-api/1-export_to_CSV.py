#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees and exporting to CSV"""

import requests
import sys
import csv

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

        # Prepare CSV file
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for todo in todos:
                task_completed_status = todo['completed']
                task_title = todo['title']
                writer.writerow({
                    "USER_ID": employee_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": task_completed_status,
                    "TASK_TITLE": task_title
                })

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

