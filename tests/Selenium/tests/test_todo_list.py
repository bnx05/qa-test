import os
import pytest

from uuid import uuid4

from page_objects.todo_list import TodoList
from .helpers import get_all_todos


TODO_URL = os.getenv('TODO_URL', 'http://localhost:8000')
SAMPLE_TODO = str(uuid4())[:8]


class TestTodoList:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.todo_list = TodoList(self.browser)

        self.browser.get(TODO_URL)

    @pytest.mark.parametrize('todo', [
        (''),
        pytest.param(' ', marks=pytest.mark.xfail(
            reason="existing bug: button is enabled even if the text is a single whitespace"))
    ])
    def test_add_invalid_todo(self, todo):
        self.todo_list.input_text(element=self.todo_list.add_todo_field, text=todo)
        assert self.browser.find_element(*self.todo_list.add_button).get_attribute("disabled")

    @pytest.mark.smoketest
    @pytest.mark.first
    def test_add_valid_todo(self):
        self.todo_list.create_new_todo(todo=SAMPLE_TODO)
        assert self.browser.find_element(*self.todo_list.first_todo_in_list).text == SAMPLE_TODO

    @pytest.mark.second
    def test_mark_todo_as_done(self):
        self.todo_list.mark_todo_as_done(todo=SAMPLE_TODO)
        assert self.browser.find_element(*self.todo_list.first_todo_in_list).get_attribute("class") == 'w-auto line-through text-green'

    @pytest.mark.third
    def test_uncheck_todo(self):
        self.todo_list.uncheck_todo(todo=SAMPLE_TODO)
        assert self.browser.find_element(*self.todo_list.first_todo_in_list).get_attribute("class") != 'w-auto line-through text-green'

    @pytest.mark.last
    def test_remove_todo(self):
        self.todo_list.remove_todo(todo=SAMPLE_TODO)

        available_todos = get_all_todos()
        if len(available_todos) > 0:
            # the first result is always the most recently created todo
            assert available_todos[0] != SAMPLE_TODO
        else:
            assert self.browser.find_element_by_css_selector('p').text == 'There are no todos'

    @pytest.mark.smoketest
    def test_verify_all_available_todos_displayed(self):
        visible_todos = self.todo_list.count_all_todos()
        todos_returned = len(get_all_todos())
        assert todos_returned == visible_todos
