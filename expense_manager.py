from models import Expense


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, date, description=""):
        expense = Expense(amount, category, date, description)
        self.expenses.append(expense)
        return expense

    def get_all(self):
        return list(self.expenses)

    def filter_expenses(self, category=None, start_date=None, end_date=None):
        results = self.expenses
        if category:
            results = [e for e in results if e.category.lower() == category.lower()]
        if start_date:
            results = [e for e in results if e.date >= start_date]
        if end_date:
            results = [e for e in results if e.date <= end_date]
        return results

    def total(self, expenses=None):
        items = self.expenses if expenses is None else expenses
        return sum(e.amount for e in items)