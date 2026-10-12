MAX_LINES = 3
MAX_BET = 200

def depsoti():
    while True:
        try:
            amount = float(input("What would you like to deposit? $")) 
            if amount >= 50 :
                break
            else:
                print("That's not enough money for this Slot Machine")
        except ValueError:
            print("That's not a real value, try again")
    return amount

def number_of_lines():
    while True:
            try:
                lines = int(input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")) 
                if 1 <= lines <= MAX_LINES :
                    break
                else:
                    print("ENTER A VALID NUMBER OF LINES")
            except ValueError:
                print("That's not a real value, try again")
    return lines

def get_bet():
    while True:
        try:
            amount = float(input("What would you like to bet on each line?")) 
            if amount <= MAX_BET :
                break
            else:
                print(f"WOAH THERE, THATS TOO MUCH MONEY (has to be under {MAX_BET})")
        except ValueError:
            print("That's not a real value, try again")
    return amount

def main():
    balance = depsoti()
    lines = number_of_lines()
    bet = get_bet()
    total_bet = bet*lines
    print(f"YOU ARE BETTING ${bet} on {lines} using your ${balance} that you deposited.\n Total bet is equal to: ${total_bet}")
    print(f"${balance}, {lines}")

if __name__ == "__main__":
    main()