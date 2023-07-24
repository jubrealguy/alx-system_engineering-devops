#!/usr/bin/python3
"""A script that returns the todo list of a given employee ID"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    completed =[todo["title"] for todo in todos if todo["completed"]]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(comp)) for comp in completed]
