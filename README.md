# Expense Tracker

A console-based Python application to add, view, filter, and export expenses.

## Features
- Add expenses (amount, category, date, description)
- View all expenses with a total
- Filter by category and/or date range
- Save and load expenses in JSON format
- Export expenses to CSV (opens in Microsoft Excel)

## Project Structure
- `main.py`: starts the application
- `cli.py`: `CLIUserInterface` class (menu and user input)
- `models.py`: `Expense` class
- `expense_manager.py`: `ExpenseManager` class (add, list, filter, total)
- `storage.py`: `Storage` class (JSON save/load and CSV export)

## How to Run
1. Open the project in VS Code.
2. Run `python main.py`.
3. Choose an option from the menu.
