#!/usr/bin/python3
"""Gather data from api"""
import json
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
        employee_name = user['username']
        user_id = user['id']
        tasks = [{"task": todo['title'], "completed": todo['completed'],
                  "username": employee_name} for todo in todos]
        data = {str(user_id): tasks}
        with open(f"{user_id}.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data exported to {user_id}.json successfully.")
    else:
        print(f"Failed to retrieve data for employee {employee_id}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
