#!/usr/bin/python3
""" Import request module """
import json
import requests
from sys import argv


def exportFullJson():
    """ returns information about his/her TODO list progress. """
    api = "https://jsonplaceholder.typicode.com/"
    reqUser = requests.get('{}users'.format(api)).json()
    reqTodo = requests.get('{}todos'.format(api)).json()

    data = {}
    for users in reqUser:
        id = users.get('id')
        username = users.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, reqTodo))
        tasks = [{'username': username,
                  'task': todo.get('title'),
                  'completed': todo.get('completed')}
                 for todo in todos]
        data['{}'.format(id)] = tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    exportFullJson()
