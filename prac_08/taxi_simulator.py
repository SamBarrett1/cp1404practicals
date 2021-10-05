"""
Practical 08 - Samuel Barrett - 13038579

Program for driving Taxis using inheritance and polymorphism
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Main program"""

    taxi_objects = [SilverServiceTaxi("FastCab", 100, 4), SilverServiceTaxi("FlashCab", 100, 6),
                    SilverServiceTaxi("LuxCab", 100, 8)]

    current_taxi = None
    total_cost = 0.00

    main_menu = ('q)uit,', 'c)hoose taxi,', 'd)rive')

    print("Let's drive!")
    print(main_menu)
    choice = input(">>> ").lower()

    while choice != 'q':
        if choice == 'c':
            print('Choose your Taxi: ')
            list_length = len(taxi_objects)
            for i in range(0, list_length):
                current_taxi = taxi_objects[i]
                print("{} - {}".format(i, current_taxi))
            taxi_choice = input(">>> ")
            if taxi_choice == '0':
                current_taxi = taxi_objects[int(taxi_choice)]
            elif taxi_choice == '1':
                current_taxi = taxi_objects[int(taxi_choice)]
            elif taxi_choice == '2':
                current_taxi = taxi_objects[int(taxi_choice)]
            else:
                print('Invalid taxi choice')
                print('Choose your Taxi: ')
                for i in range(0, list_length):
                    current_taxi = taxi_objects[i]
                    print("{} - {}".format(i, current_taxi))
                taxi_choice = input(">>> ")

            print('{} is your Taxi'.format(current_taxi.name))
            print("Bill to date: ${:.2f}".format(current_taxi.get_fare()))
            # print(main_menu)
            # taxi_choice = input(">>> ").lower()

        elif choice == 'd':
            if current_taxi is None:
                print('You need to choose a Taxi before you can drive')
                print("Bill to date: ${:.2f}".format(total_cost))
            else:
                print('Drive how far? ')
                user_distance = input(">>> ").lower()
                if user_distance.isnumeric():
                    current_taxi.drive(user_distance)
                    print('Your {} trip cost you {}'.format(current_taxi.name, current_taxi.get_fare()))
                    total_cost += current_taxi.get_fare()
                    print("Bill to date: ${:.2f}".format(total_cost))
                else:
                    print('Invalid entry')
                    print('Drive how far? ')
                    user_distance = input(">>> ").lower()
            print(main_menu)
            choice = input(">>> ").lower()
        else:
            print("Invalid option")
            print(main_menu)
            choice = input(">>> ").lower()

    print('Have a nice day')


main()

