#!/usr/bin/python3
"""Exporting data into a csv file"""
import csv
import requests
import sys


def export_csv(userId):
    """Use the provided userId as the name of the file"""
    r = requests.get('https://jsonplaceholder.typicode.com/todos/')
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")

    data = r.json()
    name = user.json().get('name')
    csv_file = f"{userId}.csv"

    with open(csv_file, mode="w", newline='') as f:
        wr = csv.writer(f)
        wr.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        for j in data:
            if j['userId'] == int(userId):
                wr.writerow([j['userId'], name, j['completed'], j['title']])


if __name__ == '__main__':
    user_id = sys.argv[1]
    export_csv(user_id)
