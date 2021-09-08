"""
Practical 06 - Samuel Barrett - 13038579
Car simulator program with class objects
"""

from prac_06.car import Car


def main():
    menu = "d) drive\n" \
           "r) refuel\n" \
           "q) quit"
    print(menu)
    user_choice = input("Enter your choice: ").lower()
    while user_choice != "q":
        if user_choice == "d":
            pass
        else:
            pass


main()
