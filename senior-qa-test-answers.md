## Establishing a testing environment

You have to guarantee the quality of  a website like ZenRooms, what are the tools and/or methods you’ll use for:

* [Define use cases](#define-use-cases)
* [Manual tests](#manual-tests)
* [Automated tests](#automated-tests)
* [Find bugs, defects, unmet requirements or unexpected behavior]
(#find-bugs-defects-unmet-requirements-or-unexpected-behavior)
* [Report about your work and targets](#report-about-your-work-and-targets)

Please give examples based on ZenRooms’ website.

## Software quality

Now that the software is bug free and fit requirements how can we be sure it is safe to release?

What are the:
* Conditions necessary to safely release it?
* Tools/methods we need to use to assess these conditions?
* Process(es) to put in place?
* Reports needed?

#

#### Define use cases

Use cases can be defined with the help of [UML use case diagrams](https://en.wikipedia.org/wiki/Use_case_diagram). 
A very simple example can be found below:

#### Manual tests

If the team is using JIRA, we can Zephyr for JIRA as the test case management tool.

We can use the following template for test cases:

Test Summary | Test Environment | Prerequisites | Steps | Test Data | Expected Result | Actual Result | Status |
------------ | ---------------- | ------------- | ----- | --------- | --------------- | ------------- | ------ |

**Test Summary**: Sign up using a valid mobile number

**Test Environment**:
- OS: Ubuntu 18.04
- Browser: Chrome v83.0.4103.61

**Prerequisites**:
- A mobile number that is unregistered with Zen Rooms

**Steps**:
1. Open https://www.zenrooms.com/
1. Click on the Sign in/Join button.
1. Select Sign up by Email or Mobile
1. Click on the Mobile tab
1. Enter the mobile number
1. Click on Get Started

**Test Data**: +639238645920

**Expected Result**:

**Actual Result**: 

**Status**: PASS

#

**Test Summary**: Sign up using an invalid mobile number

**Test Environment**:
- OS: Ubuntu 18.04
- Browser: Chrome v83.0.4103.61

**Prerequisites**:
- An invalid mobile number

**Steps**:
1. Open https://www.zenrooms.com/
1. Click on the Sign in/Join button.
1. Select Sign up by Email or Mobile
1. Click on the Mobile tab
1. Enter the mobile number
1. Click on Get Started

**Test Data**: +6620000000

**Expected Result**: User should be informed that the number is invalid

**Actual Result**: A message saying “Invalid phone number” appears

**Status**: PASS

#

**Test Summary**: Sign up using an existing mobile number

**Test Environment**:
- OS: Ubuntu 18.04
- Browser: Chrome v83.0.4103.61

**Prerequisites**:
- A valid mobile number that has previously registered with Zen Rooms

**Steps**:
1. Open https://www.zenrooms.com/
1. Click on the Sign in/Join button.
1. Select Sign up by Email or Mobile
1. Click on the Mobile tab
1. Enter the mobile number
1. Click on Get Started

**Test Data**: +639974497242

**Expected Result**: User should be informed that the number is already in use

**Actual Result**: A message “This phone number is already in user” appears

**Status**: PASS

#

#### Automated tests

For automated browser tests, we can use 
- Selenium Webdriver as the automation tool
- pytest as the test framework
- Python as the programming language

#### Find bugs, defects, unmet requirements or unexpected behavior

#### Report about your work and targets

A [low tech testing dashboard](https://www.satisfice.com/download/low-tech-testing-dashboard) can be used to communicate the 
testing efforts in a simple and easily digestible manner so that the team will actually read it. A variation of the 
dashboard may contain the following columns:

Area affected	| Components involved (with links) | Test effort | Test coverage | Quality Assessment | Comments |
------------- | -------------------------------- | ----------- | ------------- | ------------------ | -------- |
