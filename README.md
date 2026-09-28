# OOP CLI Calculator

## Purpose

This project is a Python command-line calculator for IS 218. It uses abstract classes, inheritance, polymorphism, and encapsulation to organize calculations and manage a history of previous entries. It also includes automated tests and GitHub Actions.

## Requirements

- Python 3.11 or newer
- Git
- A terminal and text editor

The setup commands below are for Ubuntu/WSL, Linux, or macOS.

## Installation

Clone the repository:

```bash
git clone https://github.com/dlg309/my-oop-calculator.git
cd my-oop-calculator
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the testing dependencies:

```bash
python -m pip install -r requirements.txt
```

Run all project commands from the `my-oop-calculator` folder. Activate the virtual environment again when opening a new terminal.

## Run the Calculator

```bash
python -m calculator
```

### Available Commands

| Command | Description |
| --- | --- |
| `add` | Add two numbers and save the calculation. |
| `subtract` | Subtract the second number from the first and save the calculation. |
| `history` | Display previous calculations with their inputs and results. |
| `remove` | Remove a calculation using its displayed number. |
| `help` | Show available commands. |
| `exit` | Close the calculator. |

### Example Session

```text
> add
First number: 10
Second number: 5
Result: 15
> subtract
First number: 20
Second number: 7
Result: 13
> history
Calculation History

1. Add: 10, 5 = 15
2. Subtract: 20, 7 = 13
> exit
Goodbye!
```

History is stored in memory for the current session and is cleared when the program exits.

The calculator uses floating-point numbers. It handles invalid numeric input, nonfinite numbers, overflowed results, and invalid removal requests. Failed calculations are not added to history. Ctrl+C and end-of-input close the program cleanly.

## Testing and Coverage

Run the tests:

```bash
python -m pytest
```

The project currently contains 37 tests covering:

- Addition and subtraction
- Abstract classes and polymorphism
- History storage and removal
- Interactive commands
- Invalid input and error recovery
- Interrupted input
- The application entry point

The `pytest.ini` configuration requires 100% line and branch coverage.

To create an HTML coverage report:

```bash
python -m pytest --cov-report=term-missing --cov-report=html
```

Open `htmlcov/index.html` to view the report.

Assertions check whether the program produces the expected behavior. Coverage shows which code was executed during testing. Full coverage does not automatically mean every requirement has been implemented correctly.

If the tests pass but coverage fails, I would inspect the missing lines and branches, identify the behavior that reaches them, and add tests with meaningful assertions.

## Design Choices

### Calculation

`Calculation` is an abstract base class. It stores the two operands and requires subclasses to implement `get_result()`.

### Add and Subtract

`Add` and `Subtract` inherit operand initialization from `Calculation`. Each class implements its own arithmetic through `get_result()`.

This supports polymorphism because the caller can use the same method without checking which operation the object represents.

### History

`History` stores calculation objects and manages adding, retrieving, and removing entries. It manages calculations instead of inheriting from `Calculation`.

The `get_history()` method returns a shallow copy of the internal list. Changing the returned list does not change which entries are stored in history. However, the calculation objects inside the two lists are still shared.

### Command-Line Interface

The CLI handles commands, input validation, output, and error messages. Arithmetic stays in the calculation classes, while collection management stays in `History`.

The `__main__.py` file starts the application when running `python -m calculator`.

## GitHub Actions

The workflow in `.github/workflows/tests.yml` runs on pushes, pull requests, and manual requests.

It installs the dependencies and runs the tests with coverage enforcement on:

- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14

[View GitHub Actions results](https://github.com/dlg309/my-oop-calculator/actions)

If a workflow fails, I would open the failing job and step and read the first useful error. An installation failure, incorrect-result assertion, and coverage failure each require a different fix.

## Design Reflection

### Where would Multiply belong?

I would add a `Multiply` class in `calculator/calculation.py`. It would inherit from `Calculation` and implement `get_result()` using multiplication.

I would also import it into the CLI, register the `multiply` command in the operations dictionary, update the help text and README, and add arithmetic and CLI tests.

`History` would not need multiplication logic because it stores calculation objects without performing their arithmetic.

### What contract could notification objects share?

`EmailNotification` and `TextNotification` could share a `send()` method. Both would accept the agreed recipient and message information and report success or failure consistently.

The caller could request that a notification be sent without knowing the delivery details. Each class would handle its own service and message format.

### What transfers to another programming language?

Separating responsibilities, grouping related state and behavior, and using shared interfaces are ideas I could apply in another language.

I would still need to learn that language's syntax and rules for constructors, types, access control, inheritance, exceptions, and object lifetime. The design ideas can transfer even when the language expresses them differently.

## Course Reference

This project follows the six-stage [IS 218 OOP calculator course](https://github.com/kaw393939/is218-oop-calculator).