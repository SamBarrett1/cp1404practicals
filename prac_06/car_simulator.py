"""
Practical 06 - Samuel Barrett - 13038579
Car simulator program with class objects
"""

from prac_06.car import Car


def main():
    menu = "Menu:\n" \
           "d) drive\n" \
           "r) refuel\n" \
           "q) quit"

    print("Let's drive")
    user_car_name = input("Enter your car name: ").title()
    user_car = Car(user_car_name, 100)
    # user_odo = user_car.odometer

    print(f"The {user_car.name}, fuel={user_car.fuel}, odo={user_car.odometer}")
    print(menu)
    user_choice = input("Enter your choice: ").lower()

    while user_choice != "q":
        if user_choice == "d":
            user_distance = int(input("How many km do you wish to drive? "))
            user_car.drive(user_distance)
            print(f"The car drove {user_car.odometer}kms")
            print()
            print(f"The {user_car.name}, fuel={user_car.fuel}, odo={user_car.odometer}")
            print(menu)
            pass
        elif user_choice == "r":
            pass
        else:
            if user_choice == "":
                print("Invalid. Choice cannot be empty")
                print(menu)
                user_choice = input("Enter your choice: ").lower()
            elif user_choice.isnumeric():
                print("Invalid. Enter a menu option")
                print(menu)
                user_choice = input("Enter your choice: ").lower()


main()
