# Selenium Tests

This folder contains the browser tests for the Todo List app. The tests use a combination Selenium Webdriver, Python and pytest.

## Setting up the environment

#### Disclaimer: This test suite has not been tested in Windows and Mac. It is recommended to run this in Linux for now.

1. Make sure you have Python 3 installed. You can check this by running `python3 --version`. The tests have been tested on Python 3.6; compatibility with previous versions is not guaranteed.
1. Creating a virtual environment is recommended to house the dependencies for the selenium tests. To create a virtual environment running on Python 3, you can install `virtualenv` first then run `virtualenv -p /usr/bin/python3 env` to create a virtual environment named `env` running on the `usr/bin/python3` binary.
1. Install the dependencies by running `pip install -r requirements.txt` inside this folder.
1. Run `pip freeze` to verify that the following have been installed successfully:
  - pytest v5.4.3
  - pytest-html v2.1.1
  - pytest-ordering v0.6
  - requests v2.23.0
  - selenium v3.141.0
  - webdriver_manager v3.1.0

## Running the tests

1. If you are using a virtual environment, enable it first by navigating to the `tests/Selenium` folder and executing `source env/bin/activate`.
1. Run all tests by calling `pytest tests/` in the command line.
  - If you want to run smoke tests only, call `pytest tests/ -m "smoketest"` in the command line.
1. If you want to see a rudimentary html report for the test run, you can append `--html=test_run.html` when running the tests. An html file will be generated after the tests have finished.
1. Screenshots will always be generated on each test run, and are found in the `screenshots` folder.
1. Basic logging is available and can be found in the `selenium.log` file.
