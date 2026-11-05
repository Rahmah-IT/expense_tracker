class CLIUserInterface:
    def print_menu(self):
        print ("Welcome to Epense Tracker")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Exit")
    def get_choice(self):
        return input("choose an option (1-3):") 