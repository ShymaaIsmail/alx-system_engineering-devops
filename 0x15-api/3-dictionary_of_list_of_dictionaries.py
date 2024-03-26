#!/usr/bin/python3
"""Gather data from api"""
import json
import requests
import sys


def get_all_tasks_for_all_users():
    """get_all_tasks_for_all_users"""
    url = f"https://jsonplaceholder.typicode.com/todos"
    users_url = f"https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users_reponse = requests.get(users_url)
    if response.status_code == 200 and users_reponse.status_code == 200:
        todos = response.json()
        users = users_reponse.json()
        json_data = {}
        for user in users:
            user_tasks = list(filter(lambda todo: todo['userId']
                              == user["id"], todos))
            tasks_details = [{"username": user["username"],
                              "task": task["title"],
                              "completed": task['completed']}
                             for task in user_tasks]
            json_data[user["id"]] = tasks_details

        with open("todo_all_employees.json", "w") as json_file:
            json.dump(json_data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data")


if __name__ == "__main__":
    get_all_tasks_for_all_users()
