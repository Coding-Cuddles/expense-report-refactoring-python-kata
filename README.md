# Expense Report Refactoring Python Kata

[![CI](https://github.com/Coding-Cuddles/expense-report-refactoring-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/expense-report-refactoring-python-kata/actions/workflows/main.yml)

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

Make sure the program still behaves the same way after your refactoring.
There's a unit test suite in place that checks that on a very rudimentary level
by just looking at the output of the program.

### Exercise 2

When you're done with refactoring, test the quality of your refactoring by
implementing two additional scenarios:

1. Extend our system to handle two more types of expenses.

   1. **Transportation**. Surcharge: 5% of the expense amount.
   2. **Supplies**. Surcharge: No surcharge.

2. Add dynamic surcharge based on day of week.

   - For dinners on weekends, the surcharge is 15% of the expense amount.
   - For breakfasts on weekends, the surcharge is 10% of the expense amount.
   - On weekdays, the surcharges remain the same as before (10% for dinner
     and 5% for breakfast).

   You may need to add a `date` field to the `Expense` class to support this
   requirement. The date should be the date when the expense occurred.

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

- [Python 3.8+](https://www.python.org/)
- [pytest](https://pytest.org)

## Usage

### Run tests

```console
make test
```
