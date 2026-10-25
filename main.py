import json
try:
     with open("expenses.json","r") as file:
          expenses = json.load(file)
except (FileNotFoundError, json.jSONDecodError):
     expenses =[]
from expense import add_expense,view_expenses
while True:
     
        print("Welcome to Expense tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("choose an option (1-3):")
        if choice == "1":
            print("Add Expense selected")
            amount, category, date = add_expense()
            expenses.append([amount, category, date])
            with open("expenses.txt", "a") as file:
                file.write(f"{amount},{category},{date}\n")
            print("Expense added successfully!")
            with open("expenses.json", "w") as file:
                json.dump(expenses, file)
        elif choice == "2":
            expenses = view_expenses()
            category_filter = input("Enter category to filter:")
            start_date = input("Enter start date (2026-10-25)")
            end_date = input("Enter end date (2026-10-25)")
            total = 0
            for expense in expenses:
                        if expense[1] == category_filter and start_date <=expense[2] <=end_date:
                            print(expense)
                            total += float(expense[0])
            print("total expenses:", total)
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid option")