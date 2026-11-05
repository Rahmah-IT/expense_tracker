from expense_manager import ExpenseManager
from storage import Storage


class CLIUserInterface:
    def __init__(self):
        self.storage = Storage()
        self.manager = ExpenseManager()
        self.manager.expenses = self.storage.load()

    def print_menu(self):
        print("\nWelcome to Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses")
        print("4. Export to CSV")
        print("5. Exit")

    def get_choice(self):
        return input("Choose an option (1-5): ")

    def add_expense(self):
        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Invalid amount.")
            return
        category = input("Category: ")
        date = input("Date (YYYY-MM-DD): ")
        description = input("Description (optional): ")
        self.manager.add_expense(amount, category, date, description)
        self.storage.save(self.manager.get_all())
        print("Expense added successfully!")

    def show_expenses(self, expenses):
        if not expenses:
            print("No expenses found.")
            return
        for e in expenses:
            print(e)
        print(f"Total: {self.manager.total(expenses):.2f}")

    def filter_expenses(self):
        category = input("Category (leave empty to skip): ")
        start = input("Start date YYYY-MM-DD (leave empty to skip): ")
        end = input("End date YYYY-MM-DD (leave empty to skip): ")
        results = self.manager.filter_expenses(
            category or None, start or None, end or None
        )
        self.show_expenses(results)

    def export_csv(self):
        self.storage.export_csv(self.manager.get_all())
        print("Exported to expenses.csv")

    def run(self):
        while True:
            self.print_menu()
            choice = self.get_choice()
            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.show_expenses(self.manager.get_all())
            elif choice == "3":
                self.filter_expenses()
            elif choice == "4":
                self.export_csv()
            elif choice == "5":
                print("Goodbye")
                break
            else:
                print("Invalid option, please try again.")