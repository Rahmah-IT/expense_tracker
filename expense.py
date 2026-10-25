import json 
def add_expense():
    amount = input("Enter expense amount:")
    category = input("Enter expense category:")
    date = input("Enter expense date (2026-10-25):")
    return [amount, category, date]

def view_expenses():
    with open ("expenses.json", "r") as file:
        expenses = json.load(file)

        return expenses