# Expense report refactoring kata in Python

[![CI](https://github.com/Coding-Cuddles/expense-report-refactoring-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/expense-report-refactoring-python-kata/actions/workflows/main.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Practice the Open-Closed Principle by refactoring an expense report without changing its behavior.
Setup is complete when all four starter tests pass.

## Overview

This kata complements [Clean Code: SOLID, Ep. 10 - Open-Closed Principle](https://cleancoders.com/episode/clean-code-episode-10).

In this exercise, you'll practice refactoring code to adhere to the Open-Closed
Principle (OCP). You'll be working with an expense report system that tracks
different types of expenses and prints a final report.

## Instructions

### Exercise 1

The `ExpenseReport` class in the `expense_report.py` file generates an expense
report. It iterates over a list of expenses, printing out a line for each
expense and totaling up the amounts.

The current implementation, however, is complex and hard to understand, and
it's not easy to modify or extend its behavior. It's your task to refactor this
code to make it cleaner and more maintainable, while ensuring that it still
correctly calculates and prints the report.

Make sure the program still behaves the same way after your refactoring. The
unit test suite checks this at a rudimentary level by examining only the
program's output.

### Exercise 2

When you're done refactoring, test the quality of your refactoring by
implementing two additional scenarios:

1. Extend our system to handle two more types of expenses.

   1. **Transportation**. Surcharge: 5% of the expense amount.
   2. **Supplies**. Surcharge: No surcharge.

2. Add dynamic surcharges based on the day of the week.

   - For dinners on weekends, the surcharge is 15% of the expense amount.
   - For breakfasts on weekends, the surcharge is 10% of the expense amount.
   - On weekdays, the surcharges remain the same as before (10% for dinner
     and 5% for breakfast).

   You may need to add a `date` field to the `Expense` class to support this
   requirement. The field should record when the expense occurred.

> [!TIP]
>
> You can use the `datetime` module in Python to work with dates, and you
> can determine if a date is a weekend by using the following function:
>
> ```python
> from datetime import datetime
>
>
> def is_weekend(date_str):
>     date = datetime.strptime(date_str, "%Y-%m-%d")
>     day_of_week = date.weekday()
>     # If day of week is 5 or 6 (Saturday or Sunday), it's a weekend
>     return day_of_week >= 5
>
> date_str = "2023-06-17"  # this is a Saturday
> print(is_weekend(date_str))  # this should print: True
> ```

## Prerequisites

Required:

- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Optional:

- [GNU Make](https://www.gnu.org/software/make/), for shorter commands. Every required task also
  has a direct `uv` command.

You do not need to install Python or pytest separately. `uv` installs a compatible Python version
and the locked project dependencies when needed.

## Set up the kata

1. Clone the repository:

   ```console
   git clone https://github.com/Coding-Cuddles/expense-report-refactoring-python-kata.git
   ```

2. Enter the repository directory:

   ```console
   cd expense-report-refactoring-python-kata
   ```

3. Run the tests. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   The first run may install Python and the project dependencies. Setup is complete when pytest
   reports `4 passed`.

   If the command fails with `uv: command not found`, install
   [uv](https://docs.astral.sh/uv/getting-started/installation/) and repeat this step.

## Work on the kata

1. Refactor `ExpenseReport` in `expense_report.py` without changing the report output.

2. Run the tests after each change. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   Continue when the test run completes without failures.

## Make command reference

Make is optional. Run `make` or `make help` to list these commands in the terminal.

| Command             | Result                                  |
| ------------------- | --------------------------------------- |
| `make all`          | Run the test suite                      |
| `make help`         | Show the command reference              |
| `make test`         | Run the test suite                      |
| `make format`       | Format tracked Python files             |
| `make format-check` | Check formatting without changing files |
| `make clean`        | Remove generated caches                 |
