# IT6039 - Testing Project for Bowling Game


## Project Description

This project is aimed at testing the functionality and performance of a Bowling Game project. It includes various test cases and scenarios to validate the correctness, compatibility, and reliability of the software.
In this project, I will try to demonstrate the following: 
* Ability to create a test plan 
* Design a suite of unit tests 
* Debug and refactor an application 
* Create Python documentation 
* Use git and report on the findings.

## Installation

* Install Python 3.8 or higher: You can download Python from the official Python website at https://www.python.org/downloads/ and follow the installation instructions for your operating system.
* Install Markdown for Code Editor (VS Code), instructions can be found here: https://code.visualstudio.com/Docs/languages/markdown.
* Configure Python tests in VS Code using Unittest: https://code.visualstudio.com/docs/python/testing.

## Usage

* Run the project in your editor (VS code).
* Follow the on-screen Description in the MarkDown documentation.
* Refer to the following guidelines for commit categories:
  * [Feature]: Commits that introduce new functionality or features to the codebase.
  * [Bugfix]: Commits that address and fix bugs or defects, syntax errors in the codebase.
  * [Refactoring]:Commits that improve the structure, design, or readability of the code without changing its functionality. 
  * [Testing]:Commits related to testing activities, such as adding or modifying test cases, fixing test failures, or improving the overall test suite.
  * [Style]:Commits that update coding style, formatting, or code conventions. This could include changes to indentation, line spacing, variable naming, or other style-related updates.
  * [Markdown]: Commits that update the Markdown file documenting the project processes
* Refer to the Test Plan section for details on testing the project.

## Test Plan

* Test Items:
  * Features or Functionality: 
•	The number of pins knocked down, and the current frame number.
•	Calculation of scores based on the rules of ten-pin bowling in diverse scenarios
•	Handling of edge cases, such as strikes, spares, and fouls.
•	Errors handling ( negative value)
•	Game starts and ends correctly.

  * Interfaces: For a bowling game, there may not be any external systems or components that need to be tested beyond the standard Python libraries.
  * Platforms or Environments: The software runs on  Windows, linux and Mac, testing will be conducted on Mac platforms for the assignment.
  * Configurations: No specific configurations or settings for this project
  * Data: Text data type
  * Test Data: Testing will be conducted using integers
  * Test Environments: Unittest framwork
  * Hardware or Software Dependencies: No dependencies, python interpreter requiered and framwork to run Unittests.
* Test Approach: 
  * Unit Testing:
 Unit testing will be used to test individual components or modules of the code, such as the BowlingGame class and its methods. This will ensure that each component works as intended and that any changes or updates to the code do not introduce unexpected errors.
  * Functional testing:
 Test cases are designed to cover various game scenarios, such as normal rolls, strikes, spares, gutter games, and special cases in the 10th frame. Inputs and outputs can be validated against expected results to ensure that the game functions as intended.
  * Boundary testing:
 Test cases are designed to cover boundary cases, such as maximum and minimum values for rolls, to ensure that the system handles them correctly and does not produce unexpected results or errors.
  * Error testing: 
 Some Test cases involves intentionally introducing errors or invalid inputs to the system to verify how it handles such situations. Test cases are designed to simulate errors, such as incorrect roll inputs or unexpected behaviour, to ensure that the system provides appropriate error handling and recovery mechanisms.
  * White Box testing:
 Test cases are designed with the knowledge of the internal implementation details of the code, the tests are designed to target specific code path.
  * Black Box testing:
 Test cases are designed based on the expected behaviour of the system, and inputs and outputs can be validated against expected results.
  * Regression testing:
 Code might need to be refactored and will involves retesting previously tested functionalities to ensure that changes or fixes do not introduce new issues or regression.
  * Acceptance Testing:
 Acceptance testing will be used to ensure that the bowling game meets the requirements and specifications provided by the stakeholders. This will involve testing the game with sample data and user scenarios to ensure that it works as expected and that all features are implemented correctly.

* Test Data: The test data for the project will include a range of scenarios and input data that cover all possible cases of playing a game of bowling
* Test Environment: 
- The test environment for the project will include the following configurations:

  * Python 3.x
  * Operating Systems: Windows, Linux, and macOS
  * IDE: VsCode or any other preferred IDE
  * Required Libraries: unittest

* Test Execution: Test will be executed using Unittests for unit testing.

## Contributing

This project if for educational purposes only, and must be completed on my own. If however, you have questions or would like to participate to this project after April 2023, please feel free to contact me for more details on how to contribute.

## License

No specific license for this project, code has been provided by Whitecliffe Technology, NZ for educational purpose only.

## Acknowledgements

Thank you to Vivian Wang, for providing all the resources and support through this course.

## Contact Information

Please feel free to reach out for questions, feedback or support at the following email address: sper211@mywhitecliffe.com
