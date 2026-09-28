# OOP CLI Calculator
Purpose
This project is a Python command-line calculator for my IS 218 course. It uses abstract classes, inheritance, polymorphism, and encapsulation to organize calculations and manage a history of previous entries. The project includes automated tests and a GitHub Actions workflow.
Requirements
- Python 3.11 or newer
- Git
- A terminal and text editor
The setup commands below are for Ubuntu/WSL, Linux, or macOS.
Installation
Clone the repository and open the project folder:
git clone https://github.com/dlg309/my-oop-calculator.git
cd my-oop-calculator
Create and activate a virtual environment:
python3 -m venv .venv
source .venv/bin/activate
Install the testing dependencies:
python -m pip install -r requirements.txt
Run project commands from the folder containing calculator/, tests/, and pytest.ini. When opening a new terminal, return to this folder and activate .venv again.
Run the Calculator
python -m calculator
Command	Description
add	Add two numbers and save the calculation.
subtract	Subtract the second number from the first and save the calculation.
history	Display saved calculations with their operation, inputs, and result.
remove	Remove a calculation using its displayed number.
help	Display the available commands.
exit	Close the calculator.


Example session:
> add
First number: 10
Second number: 5
Result: 15
> history
Calculation History

1. Add: 10, 5 = 15
> remove
Calculation History

1. Add: 10, 5 = 15
Enter calculation number to remove: 1
Removed: Add: 10, 5 = 15
> exit
Goodbye!
History stays in memory during the current session and is cleared when the program exits. The calculator uses floating-point numbers. Invalid numeric input, nonfinite values, overflowed results, and invalid removal requests are handled without ending the session. Failed calculations are not saved. Ctrl+C and end-of-input close the application cleanly.
Testing and Coverage
Run the tests:
python -m pytest
The suite currently contains 37 tests covering arithmetic, abstract-class behavior, history management, CLI interactions, and error handling. The pytest.ini configuration requires 100% line and branch coverage. A run fails if a test fails or coverage falls below the requirement.
Assertions compare actual behavior with expected behavior. For example, a removal test checks that the selected object is returned and the remaining entries stay in order. Coverage identifies code that was not executed; it does not prove that every requirement has been implemented correctly.
To generate an HTML coverage report:
python -m pytest --cov-report=term-missing --cov-report=html
Open htmlcov/index.html to view the report. If tests pass but coverage fails, inspect the missing lines and branches, identify the behavior that would execute them, and add meaningful assertions for that behavior.
Design Choices
Component	Responsibility
Calculation	Stores operands and defines the abstract get_result() method.
Add and Subtract	Inherit operand initialization and implement their own arithmetic.
History	Stores calculation objects and controls adding, retrieving, and removing entries.
CLI	Reads commands, validates input, displays results, and handles errors.
__main__.py	Starts the calculator when running python -m calculator.


The operation classes use the same method name, so the caller can request a result without checking each object's type. This is polymorphism.
History manages calculations instead of inheriting from Calculation. Its get_history() method returns a shallow copy of the internal list. Clearing the returned list does not erase the stored entries, but both lists still reference the same calculation objects.
GitHub Actions
The workflow in .github/workflows/tests.yml runs on pushes, pull requests, and manual requests. It installs dependencies and runs the coverage-enforced test suite on Python 3.11, 3.12, 3.13, and 3.14.
View workflow results
For a failed run, I would open the failing job and step, then read the first useful error. An installation error, failed assertion, and coverage failure require different fixes.
Design Reflection
Adding multiplication
I would add a Multiply class in calculator/calculation.py that inherits from Calculation and implements get_result() using multiplication. I would also import the class into the CLI, register the multiply command in the operations dictionary, update the help text and README, and add arithmetic and CLI tests. History would not need multiplication logic because it stores calculation objects without performing their arithmetic.
Sharing a notification contract
EmailNotification and TextNotification could share a send() method. Both would accept the agreed recipient and message information and report success or failure consistently. The caller could request that a notification be sent without needing to know the delivery details. Each implementation would handle its own service and message format.
Applying the design in another language
Separating responsibilities, keeping related state and behavior together, and using a shared interface are ideas I could apply in another language. I would still need to learn that language's rules for constructors, types, access control, inheritance, exceptions, and object lifetime. The design ideas can transfer even when the syntax and runtime behavior differ.
Course Reference
This project follows the six-stage IS 218 OOP calculator course.