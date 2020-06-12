## Establishing a testing environment

You have to guarantee the quality of  a website like ZenRooms, what are the tools and/or methods you’ll use for:

* [Define use cases](#define-use-cases)
* [Manual tests](#manual-tests)
* [Automated tests](#automated-tests)
* [Find bugs, defects, unmet requirements or unexpected behavior](#find-bugs-defects-unmet-requirements-or-unexpected-behavior)
* [Report about your work and targets](#report-about-your-work-and-targets)

Please give examples based on ZenRooms’ website.

## Software quality

Now that the software is bug free and fit requirements how can we be sure it is [safe to release?](#ensuring-software-quality)

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
- The mobile number should receive a verification code via SMS.
- The user should proceed to the Password Setup form after entering the verification code in the modal.

**Actual Result**:
- The mobile number received a verification code.
- The user was asked to complete the Password Setup form after providing the verification code.

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

For automated api tests, the basic approach would be to use an existing http library. For Python projects, an example would be the Requests library. 

#### Find bugs, defects, unmet requirements or unexpected behavior

In a fast-paced environment, one approach would be to use risk-based testing to ensure that the features with the most business risk get more attention and are tested thoroughly instead of the those which have lower impact on business and customers.

One way to ensure that adequate testing can be done is to make the developers involved in the testing process. Ideally, before anything gets merged to the testing environment, the developers have ensured that the acceptance criteria have been met and sanity has been applied to their code changes so no time is wasted and the QA team can focus on risk-based and exploratory testing on the product.

#### Report about your work and targets

A [low tech testing dashboard](https://www.satisfice.com/download/low-tech-testing-dashboard) can be used to communicate the 
testing efforts in a simple and easily digestible manner so that the team will actually read it. A variation of the 
dashboard may contain the following columns:

Area affected	| Components involved (with links) | Test effort | Test coverage | Quality Assessment | Comments |
------------- | -------------------------------- | ----------- | ------------- | ------------------ | -------- |

#### Ensuring software quality

What are the conditions necessary to safely release it?
- No regression bugs have been found in the software build/s.
- Automated tests have passed.
  - Automated tests (unit/integration/end-to-end) should be integrated in the CI/CD so that they will run for each build or deployment.
  - Reporting of test results should be automatically made available and accessible so there is no delay in addressing them if there are any failures reported.
- Test report has been reviewed and sign off has been given by stakeholders.
  - After the QA team has successfully done testing and has submitted the test report, relevant stakeholders should give the thumbs up to indicate that the release is to proceed as planned.
- Artifacts are properly tagged.
  - Git tags should be used in repositories so we can easily create Releases off of it, and easily do any rollback if it is needed.
- Deployment checklist is ready.
  - A checklist of things to do before and after any deployment should be created or updated.
  - Typical things in this checklist include:
    - Any database changes that need to be done manually
    - New environment variables to be added
    - Any configuration that need to be added/updated
- Post deploy smoke tests are ready.
  - Smoke tests to ensure that the system is up and running and critical functionalities are in place.
  - Ideally these smoke tests are already automated. If there are some that need to be done manually then those should be performed ASAP after deployment.
- Alerts are in place.
  - The team should be alerted for each deployment’s status.
  - If there are any critical issues, there should be an alert created for those so that the team will know ASAP and can fix the issues before the customers see them.
- Rollback plan is in place.
  - In the worst case scenario where a deployment failed or there are production issues, a rollback can be done immediately and there is no significant downtime for customers.
- Customers have been informed ahead of time if there is any planned outage related to the release.
  - If the release is a major one and there is significant downtime involved, existing customers should be informed several days in advance.
  - A “maintenance” page should also be put up so that if a customer accesses the site during the planned downtime, they will see a nice UI informing them of the downtime and when to check back again.
  - Customers should also be informed after the planned downtime has been finished.

What are the tools/methods we need to use to assess these conditions?
- Checklists 
  - Pre and post deployment checklists as mentioned above should be in place.
- Automated tests integrated in the CI/CD pipeline to make sure that
  - they run for each build (unit/integration tests) and each deploy (end-to-end tests)
  - specific smoke tests run post deploy for faster feedback
-Slack integration: statuses are communicated ASAP
  - Test runs, build statuses and deploy statuses should show up in Slack ASAP
  - If there are any system alerts, they should be reported in Slack as well

What are the processes to put in place?
- Pre and post deployment checklists
- Reporting/escalation process: determine
  - Who should monitor the deployments
  - Who should conduct the post deploy testing
  - Who should be informed if any problems arise post deploy
  - What should be done if any problems are encountered
  - What should be documented post deploy
  - Who should initiate postmortems, if any
- Post deployment process
  - Release notes: determine
    - What details should be included
    - Who should create the release notes
    - Who should be informed of the release

What are the reports needed?
- Test summary report.
- Release notes planned to be sent out after deployment, containing details on the features, enhancements, and bug fixes included in the release.

