import pytest
import textwrap

from expense_report import ExpenseReport, Expense, ExpenseType, ReportPrinter


class MockReportPrinter(ReportPrinter):

    def __init__(self):
        self.text = ""

    def print(self, text):
        self.text += f"{text}\n"


@pytest.fixture
def report():
    return ExpenseReport()


@pytest.fixture
def printer():
    return MockReportPrinter()


def test_print_empty(report, printer):
    report.print_report(printer)

    expected_output = textwrap.dedent("""
        Expense Report
        --------------
        --------------
        Meal Total: 0.00
        Total: 0.00
    """)
    assert printer.text == expected_output.lstrip()


def test_print_one_dinner(report, printer):
    report.add_expense(Expense(ExpenseType.DINNER, 3000))
    report.print_report(printer)

    expected_output = textwrap.dedent("""
        Expense Report
        --------------
        Dinner\t30.00\t
        --------------
        Meal Total: 33.00
        Total: 33.00
    """)
    assert printer.text == expected_output.lstrip()


def test_print_two_meals_and_dinner_over(report, printer):
    report.add_expense(Expense(ExpenseType.DINNER, 6000))
    report.add_expense(Expense(ExpenseType.BREAKFAST, 1000))
    report.print_report(printer)

    expected_output = textwrap.dedent("""
        Expense Report
        --------------
        Dinner\t60.00\tX
        Breakfast\t10.00\t
        --------------
        Meal Total: 76.50
        Total: 76.50
    """)
    assert printer.text == expected_output.lstrip()


def test_print_mix_and_dinner_over(report, printer):
    report.add_expense(Expense(ExpenseType.DINNER, 5000))
    report.add_expense(Expense(ExpenseType.BREAKFAST, 2000))
    report.add_expense(Expense(ExpenseType.LODGING, 3000))
    report.print_report(printer)

    expected_output = textwrap.dedent("""
        Expense Report
        --------------
        Dinner\t50.00\t
        Breakfast\t20.00\tX
        Lodging\t30.00\t
        --------------
        Meal Total: 76.00
        Total: 110.50
    """)
    assert printer.text == expected_output.lstrip()
