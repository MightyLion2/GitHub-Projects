import csv
"""Create a main menu loop with choices: Add Expense, View Summary, Export CSV, Exit.
Store transactions in a list of dictionaries with category, amount, and description.
Use `try-except` blocks to handle non-numeric input safely.
Write a helper function to export data into a `expenses.csv` file using standard Python `csv` module."""

IsRunning = True
data = {}

def main():
    while IsRunning:
        print("=== EXPENSE TRACKER ===")
        print("1. Add Expense\n2. View Summary\n3. Export CSV\n4. Exit")
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            export_csv()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


def export_csv():
    pass

def add_expense():
    while True:
        expense = input("enter an expense: ")
        if expense == "q".strip():
            break
        data["Expenses"] = expense
        description = input("enter a description for this expense: ")
        data["Descriptions"] = description
        price = float(input("What is the price of this expense: $"))
        data["Prices"] = price
def exit_menu():
    pass

def show_summary():
    print("--------------------------------- YOUR EXPENSES ---------------------------------")
    for values in data.values():
        print(values)
    print("---------------------------------------------------------------------------------")
if __name__ == "__main__":
    main()