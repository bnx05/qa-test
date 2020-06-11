import os
import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def set_browser():
    selected_browser = os.getenv('BROWSER', 'chrome').lower()

    if selected_browser == 'chrome':
        wd = webdriver.Chrome(ChromeDriverManager().install())
    elif selected_browser == 'firefox':
        wd = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise Exception(
            "{} not yet supported! Please select either Chrome or Firefox".format(selected_browser))

    wd.maximize_window()

    return wd


@pytest.fixture
def browser(request):
    with set_browser() as browser:
        yield browser
        browser.save_screenshot(
            time.strftime('./%b-%d-%Y-%H:%M_{}.png'.format(request.node.name)))
