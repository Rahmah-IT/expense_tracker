class CLIUserInterface:
    def print_menu(self):
        print ("Welcome to Epense Tracker")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Exit")
    def get_choice(self):
        return input("choose an option (1-3):")
    def run(self):
        while True:
            self.print_menu()
            choice = self .get_choice()
            if choice == "1":
                print("Add expense: coming soon")
            elif choice == "2":
                print("view expense: coming soon")
            elif choice == "3":
                print("Goodbye")
                break
        else:
            print("Invalid option, pleasw try again.")