import os
import pytest
import requests

from uuid import uuid4

from page_objects.todo_list import TodoList


TODO_URL = os.getenv('TODO_URL', 'http://localhost:8000')
SAMPLE_TODO = str(uuid4())[:8]


class TestTodoList:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.todo_list = TodoList(self.browser)

        self.browser.get(TODO_URL)

    @pytest.mark.first
    def test_add_todo(self):
        self.todo_list.create_new_todo(todo=SAMPLE_TODO)
        assert self.browser.find_element(
            *self.todo_list.first_todo_in_list).text == SAMPLE_TODO

    @pytest.mark.second
    def test_mark_todo_as_done(self):
        self.todo_list.mark_todo_as_done(todo=SAMPLE_TODO)
        assert self.browser.find_element(
            *self.todo_list.first_todo_in_list).get_attribute("class") == 'w-auto line-through text-green'

    @pytest.mark.third
    def test_uncheck_todo(self):
        self.todo_list.uncheck_todo(todo=SAMPLE_TODO)
        assert self.browser.find_element(
            *self.todo_list.first_todo_in_list).get_attribute("class") != 'w-auto line-through text-green'

    @pytest.mark.last
    def test_remove_todo(self):
        self.todo_list.remove_todo(todo=SAMPLE_TODO)

        # query the api to get the available list of todos
        # the first result is always the most recently created todo
        r = requests.get('{}/todos'.format(TODO_URL))
        available_todos = [todo['text'] for todo in r.json()]
        assert available_todos[0] != SAMPLE_TODO
