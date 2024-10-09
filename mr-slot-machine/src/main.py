import time

from utility.config import MAX_BET, MIN_BET
from utility.slot_machine import SlotMachine


def main():
    print("Welcome to The Slot Machine!")
    print()
    print(r"by:  __    __  ______     __  __  __  ______ ______     ")
    print(r'    /\ "-./  \/\  == \   /\ \/\_\_\_\/\__  _/\  == \    ')
    print(r"    \ \ \-./\ \ \  __<  _\_\ \/_/\_\/\/_/\ \\ \  __<    ")
    print(r"     \ \_\ \ \_\ \_\ \_/\_____\/\_\/\_\ \ \_\\ \_\ \_\  ")
    print(r"      \/_/  \/_/\/_/ /_\/_____/\/_/\/_/  \/_/ \/_/ /_/  ")
    print("                                                  @mrjxtr")
    print()
    time.sleep(2)
    print("HERE ARE THE RULES:")
    time.sleep(1)
    print("1. Deposit as much as you want.")
    time.sleep(0.5)
    print("2. You can bet on up to 3 lines.")
    time.sleep(0.5)
    print(f"3. You can bet ${MIN_BET} to ${MAX_BET} per line.")
    time.sleep(0.5)
    print("4. Play until your balance is $0 or walk out with your winnings.")
    print()
    time.sleep(1)
    print("POINTS SYSTEM:")
    time.sleep(1)
    print("A: 10 points")
    time.sleep(0.5)
    print("B: 8 points")
    time.sleep(0.5)
    print("C: 6 points")
    time.sleep(0.5)
    print("D: 4 points")
    time.sleep(0.5)
    print()
    time.sleep(2)

    sm = SlotMachine()
    balance = sm.deposit()
    while True:
        if balance > 0:
            print()
            print(f"Current balance is ${balance}")
            choice = input("Do you want to continue? ([y]/n): ").lower()

            if choice in ["", "y", "yes"]:
                balance += sm.spin(balance)
            elif choice in ["n", "no"]:
                print()
                restart = input("Do you want to exit? ([y]/n): ").lower()
                if restart in ["", "y", "yes"]:
                    print()
                    print(f"You left with ${balance}")
                    print()
                    time.sleep(1)
                    return  # Exit the program
                elif restart in ["n", "no"]:
                    continue  # Continue the loop
                else:
                    print("please enter 'y' or 'n'.")
            else:
                print("please enter 'y' or 'n'.")
        else:
            print()
            print(f"Your balance is ${balance}.")
            choice = input("Do you want to deposit more money? ([y]/n): ").lower()
            if choice in ["", "y", "yes"]:
                balance = sm.deposit()
            elif choice in ["n", "no"]:
                print()
                time.sleep(1)
                print("Thank you for playing The Slot Machine!")
                print()
                print(r"by:  __    __  ______     __  __  __  ______ ______     ")
                print(r'    /\ "-./  \/\  == \   /\ \/\_\_\_\/\__  _/\  == \    ')
                print(r"    \ \ \-./\ \ \  __<  _\_\ \/_/\_\/\/_/\ \\ \  __<    ")
                print(r"     \ \_\ \ \_\ \_\ \_/\_____\/\_\/\_\ \ \_\\ \_\ \_\  ")
                print(r"      \/_/  \/_/\/_/ /_\/_____/\/_/\/_/  \/_/ \/_/ /_/  ")
                print("                                                  @mrjxtr")
                print()
                time.sleep(1)
                break
            else:
                print("please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
