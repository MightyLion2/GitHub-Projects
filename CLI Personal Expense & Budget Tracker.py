import csv
import pandas as P
"""Create a main menu loop with choices: Add Expense, View Summary, Export CSV, Exit.
Store transactions in a list of dictionaries with category, amount, and description.
Use `try-except` blocks to handle non-numeric input safely.
Write a helper function to export data into a `expenses.csv` file using standard Python `csv` module."""
file_path = "C:/Users/felix/Downloads/CLI Personal Expense & Budget Tracker.csv"
IsRunning = True
Expenses = []
Descriptions = []
Prices = []
data = {"Expenses": Expenses,
            "Descriptions": Descriptions,
            "Prices": Prices}

def main():
    while IsRunning:
        print("=== EXPENSE TRACKER ===")
        print("1. Add Expense\n2. View Summary\n3. Export to new CSV\n4. Exit\n5. Export to existing CSV")
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
        elif choice == '5':
            edit()
        else:
            print("Invalid choice, try again.\n")

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
    df = P.DataFrame(data)
    print("--------------------------------- YOUR EXPENSES ---------------------------------")
    print(df.to_string(index=False))
    print("---------------------------------------------------------------------------------")

def export_csv():
    # try:
    #    with open(file_path, "w") as file:
    #     writer = csv.writer(file)

    #     # headers = list(data.keys())
    #     # writer.writerow(headers)
    
    #     # rows = zip(*data.values())
    #     # writer.writerows(rows)

    
    # except FileExistsError:
    #     print(f"That file already exists!")
    # return writer
    df = P.DataFrame(data)
    try:
        df.to_csv(file_path, mode='x', index=False)
    except FileExistsError:
        print()
        print("THIS FILE ALREADY EXISTS, USE:\n'Export to existing CSV'")
        print()

def edit():
   df = P.DataFrame(data)
   df.to_csv(file_path, mode='a', index=False, header=False)
    # df2 = P.read_csv(file_path)

    # print(df2)

    # df2.to_csv("C:/Users/felix/Downloads/Modified.csv")


if __name__ == "__main__":
    main()