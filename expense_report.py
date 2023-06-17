from abc import ABC, abstractmethod
from enum import Enum, auto


class ReportPrinter(ABC):

    @abstractmethod
    def print(self, text):
        pass


class ExpenseType(Enum):
    DINNER = auto()
    BREAKFAST = auto()
    LODGING = auto()


class Expense:

    def __init__(self, type, amount):
        self.type = type
        self.amount = amount


class ExpenseReport:

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def print_report(self, printer):
        printer.print("Expense Report")
        printer.print("--------------")

        total = 0
        meal_total = 0
        for expense in self.expenses:
            surcharge = 0
            name = ""
            if expense.type == ExpenseType.DINNER:
                surcharge = expense.amount * 0.10
                name = "Dinner"
            elif expense.type == ExpenseType.BREAKFAST:
                surcharge = expense.amount * 0.05
                name = "Breakfast"
            elif expense.type == ExpenseType.LODGING:
                surcharge = expense.amount * 0.15
                name = "Lodging"
            else:
                name = "Other"

            total += expense.amount + surcharge
            if expense.type == ExpenseType.DINNER or expense.type == ExpenseType.BREAKFAST:
                meal_total += expense.amount + surcharge

            meal_over_expenses_marker = ("X" if
                                         (expense.type == ExpenseType.DINNER
                                          and expense.amount > 5000) or
                                         (expense.type == ExpenseType.BREAKFAST
                                          and expense.amount > 1000) else "")

            printer.print(
                f"{name}\t{expense.amount / 100:.2f}\t{meal_over_expenses_marker}"
            )

        printer.print("--------------")
        printer.print(f"Meal Total: {meal_total / 100:.2f}")
        printer.print(f"Total: {total / 100:.2f}")
