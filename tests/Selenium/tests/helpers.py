import requests


API = 'http://localhost:8000'
TODO_ENDPT = '/todos'


def get_all_todos():
    r = requests.get('{}{}'.format(API, TODO_ENDPT))
    return r.json()
