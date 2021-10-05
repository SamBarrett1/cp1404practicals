"""
Practical 08 - Samuel Barrett - 13038579

Program for driving Taxis using inheritance and polymorphism
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Main program"""
    fast_taxi = SilverServiceTaxi("FastCab", 100, 4)
    flash_taxi = SilverServiceTaxi("FlashCab", 100, 6)
    lux_taxi = SilverServiceTaxi("LuxCab", 100, 8)

    taxi_objects = [fast_taxi, flash_taxi, lux_taxi]

    current_taxi = None
    total_cost = 0.00

    main_menu = ('q)uit,', 'c)hoose taxi,', 'd)rive')
    taxi_menu = ('Choose your Taxi:\n'
                 '1. FastCab\n'
                 '2. FlashCab\n'
                 '3. LuxCab')

    print("Let's drive!")
    print(main_menu)
    choice = input(">>> ").lower()

    while choice != 'q':
        if choice == 'c':
            while not current_taxi:
                print('Choose your Taxi: ')
                for taxi in enumerate(taxi_objects, start=0):
                    print(taxi)
                if choice == '0':
                    current_taxi = taxi_objects[0]
                    pass
                elif choice == '1':
                    current_taxi = taxi_objects[1]
                    pass
                elif choice == '2':
                    current_taxi = taxi_objects[2]
                    pass
                else:
                    print("Invalid option")
                    print(taxi_menu)
                    choice = input(">>> ")
            current_fare = current_taxi.get_fare()
            print("Bill to date: ${:.2f}".format(current_fare))
            print(main_menu)
            choice = input(">>> ").lower()

        elif choice == 'd':
            if not current_taxi:
                print('You need to choose a Taxi before you can drive')
                print("Bill to date: ${:.2f}".format(total_cost))
                print(main_menu)
                choice = input(">>> ").lower()
            else:
                print('Drive how far? ')
                user_distance = input(">>> ").lower()
                current_taxi.drive(user_distance)
                pass
                print('Your {} trip cost you {}'.format(current_taxi.name, current_taxi.get_fare()))
                total_cost += current_taxi.get_fare()
                print("Bill to date: ${:.2f}".format(total_cost))
            print(main_menu)
            choice = input(">>> ").lower()
        else:
            print("Invalid option")
            print(main_menu)
            choice = input(">>> ").lower()

        print('Have a nice day')


main()

