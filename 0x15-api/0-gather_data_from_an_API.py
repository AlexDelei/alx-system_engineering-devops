#!/usr/bin/python3
""" API call and display of data"""
import requests
import sys


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
    done = len(done_list)
    total = len(not_done) + done
    print("Employee {} is done with tasks {}/{}:".format(name, done, total))
    for i in task_title:
        print("\t{}".format(i))


if __name__ == "__main__":
    user_id = sys.argv[1]
    getUser(user_id)
