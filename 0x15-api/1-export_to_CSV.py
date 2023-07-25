#!/usr/bin/python3
"""A script that exports the todo list of a given employee ID to CSV"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    USER_ID = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    USERNAME = user.get("username")
    todos = requests.get(url + "todos", params={"userId": USER_ID}).json()

    with open("{}.csv".format(USER_ID), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [USER_ID, USERNAME, todo.get("completed"), todo.get("title")]
         ) for todo in todos]
