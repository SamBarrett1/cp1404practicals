"""
Practical 08 - Samuel Barrett - 13038579
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Program for driving Taxis using inheritance and polymorphism"""

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
            taxi_choice = int(input(">>> "))
            try:
                current_taxi = taxi_objects[taxi_choice]
            except IndexError:
                print('Invalid taxi choice')
            print('{} is your Taxi'.format(current_taxi.name))

        elif choice == 'd':
            if current_taxi:
                current_taxi.start_fare()
                print('Drive how far? ')
                user_distance = int(input(">>> "))
                current_taxi.drive(user_distance)
                print('Your {} trip cost you ${:.2f}'.format(current_taxi.name, current_taxi.get_fare()))
            else:
                print('You need to choose a Taxi before you can drive')
        else:
            print("Invalid option")
        total_cost += current_taxi.get_fare()
        print("Bill to date: ${:.2f}".format(total_cost))
        print(main_menu)
        choice = input(">>> ").lower()

    print('Total trip cost: ${:.2f}'.format(total_cost))
    print('Taxis are now')
    list_length = len(taxi_objects)
    for i in range(0, list_length):
        current_taxi = taxi_objects[i]
        print("{} - {}".format(i, current_taxi))
    print('Have a nice day')


main()

