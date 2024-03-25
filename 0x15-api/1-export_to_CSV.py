#!/usr/bin/python3
""" API call and display of data"""
import csv
import requests
import sys


def export_csv(userId, data, username):
    """Export data to CSV file"""
    csv_file = f"{userId}.csv"
    with open(csv_file, mode="w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in data:
            writer.writerow([userId, username, task['completed'], task['title']])


def getUser(userId):
    """print out how many todos a certain user has done"""
    r = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos/')

    tasks_done = tasks.json()
    done_list = []
    not_done = []
    task_title = []
    for i in tasks_done:
        if i['userId'] == int(userId):
            if i['completed']:
                done_list.append(i['completed'])
                task_title.append(i['title'])
            else:
                not_done.append(i['completed'])

    data = r.json()
    name = data.get('name')
    username = data.get('username')
    export_csv(userId, tasks_done, username)
    done = len(done_list)
    total = len(not_done) + done


if __name__ == "__main__":
    user_id = sys.argv[1]
    getUser(user_id)
