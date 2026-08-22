import csv
import pandas as P
"""Create a main menu loop with choices: Add Expense, View Summary, Export CSV, Exit.
Store transactions in a list of dictionaries with category, amount, and description.
Use `try-except` blocks to handle non-numeric input safely.
Write a helper function to export data into a `expenses.csv` file using standard Python `csv` module."""

IsRunning = True
Expenses = []
Descriptions = []
Prices = []

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
        Expenses.append(expense)
        description = input("enter a description for this expense: ")
        Descriptions.append(description)
        price = float(input("What is the price of this expense: $"))
        Prices.append(price)
def exit_menu():
    pass

def show_summary():
    data = {"Expenses": Expenses,
            "Descriptions": Descriptions,
            "Prices": Prices}
    df = P.DataFrame(data)
    print("--------------------------------- YOUR EXPENSES ---------------------------------")
    print(df.to_string(index=False))
    print("---------------------------------------------------------------------------------")
if __name__ == "__main__":
    main()