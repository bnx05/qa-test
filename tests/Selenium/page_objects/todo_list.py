from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base import Base


class TodoList(Base):
    add_button = (By.CSS_SELECTOR, 'button')
    add_todo_field = (By.CSS_SELECTOR, 'input')
    all_todos = (By.CSS_SELECTOR, '#app div.mb-4')
    first_todo_in_list = (
        By.XPATH, '//div[@id="app"]//div[@class="mb-4"][1]//p')

    def count_all_todos(self):
        return len(self.browser.find_elements(*self.all_todos))

    def create_new_todo(self, todo):
        self.input_text(element=self.add_todo_field, text=todo)
        self.click(element=self.add_button)
        self.wait.until(EC.text_to_be_present_in_element(
            self.first_todo_in_list, todo))

    def mark_todo_as_done(self, todo):
        # for duplicate todos, this will always check the latest one
        todo_locator = '(//p[text()="{}" and @class[contains(., "text-grey-darkest")]])[1]'.format(todo)
        todo_checkbox_locator = (
            By.XPATH, '{}/preceding-sibling::input[@type="checkbox"]'.format(todo_locator))
        self.click(element=todo_checkbox_locator)

    def remove_todo(self, todo):
        # for duplicate todos, this will always remove the latest one
        todo_locator = '(//p[text()="{}"])[1]'.format(todo)
        todo_remove_locator = (
            By.XPATH, '{}/following-sibling::button'.format(todo_locator))
        self.click(element=todo_remove_locator)

    def uncheck_todo(self, todo):
        # for duplicate todos, this will always remove the latest one
        todo_locator = '(//p[text()="{}" and @class[contains(., "line-through")]])[1]'.format(todo)
        todo_checkbox_locator = (
            By.XPATH, '{}/preceding-sibling::input[@type="checkbox"]'.format(todo_locator))
        self.click(element=todo_checkbox_locator)
