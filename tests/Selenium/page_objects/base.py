from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 2)

    def clear(self, element):
        self.wait.until(EC.element_to_be_clickable(element)).clear()

    def click(self, element):
        self.wait.until(EC.element_to_be_clickable(element)).click()

    def input_text(self, element, text=''):
        self.click(element)
        self.clear(element)
        self.browser.find_element(*element).send_keys(text)
