#!/usr/bin/python3
"""Fetch all records for all users"""
import json
import requests


def getAll():
    """Fetch evrything"""
    user_id = 1
    data = {}

    while True:
        url = 'https://jsonplaceholder.typicode.com/'
        users = f"users?id={user_id}"
        todos = f"todos?userId={user_id}"

        userData = requests.get(f"{url}{users}").json()
        if not userData:
            break
        userName = userData[0].get("username")
        todosData = requests.get(f"{url}{todos}").json()

        data[user_id] = [
                {
                    "username": userName,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                for task in todosData
            ]
        user_id += 1

        with open("todo_all_employees.json", "w") as f:
            json.dump(data, f)


if __name__ == '__main__':
    getAll()
