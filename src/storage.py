import csv
import json

from src.models import Expense


class Storage:
    def __init__(self, filename="expenses.json"):
        self.filename = filename

    def save(self, expenses):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([e.to_dict() for e in expenses], file, indent=4)

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            return [Expense.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def export_csv(self, expenses, csv_filename="expenses.csv"):
        with open(csv_filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "category", "amount", "description"])
            for e in expenses:
                writer.writerow([e.date, e.category, e.amount, e.description])