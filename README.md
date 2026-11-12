# Expense Tracker

A console-based Python application to add, view, filter, and export expenses.

## Features
- Add expenses (amount, category, date, description)
- View all expenses with a total
- Filter by category and/or date range
- Save and load expenses in JSON format
- Export expenses to CSV (opens in Microsoft Excel)

## Project Structure
- `src/main.py`: starts the application
- `src/cli.py`: `CLIUserInterface` class (menu and user input)
- `src/models.py`: `Expense` class
- `src/expense_manager.py`: `ExpenseManager` class (add, list, filter, total)
- `src/storage.py`: `Storage` class (JSON save/load and CSV export)

## How to Run
From the project root:

    python -m src.main
