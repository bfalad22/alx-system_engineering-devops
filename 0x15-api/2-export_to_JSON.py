#!/usr/bin/python3
""" Import request module """
import json
import requests
from sys import argv


def exportJson():
    """ returns information about his/her TODO list progress. """
    api = "https://jsonplaceholder.typicode.com/"
    if (len(argv) > 1):
        id = int(argv[1])
        reqUser = requests.get('{}users/{:d}'.format(api, id)).json()
        reqTodo = requests.get('{}todos'.format(api),
                               params={'userId': id}).json()
        data = {id: [{'task': todo.get('title'),
                      'completed': todo.get('completed'),
                      'username': reqUser.get('username')}
                     for todo in reqTodo]}

        with open('{}.json'.format(id), 'w') as file:
            json.dump(data, file)


if __name__ == "__main__":
    exportJson()
