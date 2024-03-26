#!/usr/bin/python3
"""Gather data from api"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """get_employee_todo_progress"""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        todos = response.json()
        employee_name = todos[0]['userId']
        done_tasks = [todo['title'] for todo in todos if todo['completed']]
        total_tasks = len(todos)
        number_of_done_tasks = len(done_tasks)
        print(f"Employee {employee_name} is done with tasks \
                ({number_of_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task}")
    else:
        print(f"Failed to retrieve data for employee {employee_id}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
