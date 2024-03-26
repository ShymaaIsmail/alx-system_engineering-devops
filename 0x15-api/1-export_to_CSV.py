#!/usr/bin/python3
"""Gather data from api"""
import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """get_employee_todo_progress"""
    user_api = "https://jsonplaceholder.typicode.com/users/" + str(employee_id)
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    user_details = requests.get(user_api)
    if response.status_code == 200 and user_details.status_code == 200:
        todos = response.json()
        user = user_details.json()
        employee_name = user['name']
        done_tasks = [(todo['title'], todo['completed']) for todo in todos]
        total_tasks = len(todos)
        number_of_done_tasks = sum(1 for task, completed in
                                   done_tasks if completed)
        print(f"Employee {employee_name} is done with tasks"
              f"({number_of_done_tasks}/{total_tasks}):")

        # Exporting to CSV
        csv_file_name = f"{employee_id}.csv"
        with open(csv_file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for task, completed in done_tasks:
                writer.writerow([employee_id,
                                 employee_name,
                                 'Completed' if completed else 'Incomplete',
                                 task])

        print(f"Data exported to {csv_file_name}")
    else:
        print(f"Failed to retrieve data for employee {employee_id}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
