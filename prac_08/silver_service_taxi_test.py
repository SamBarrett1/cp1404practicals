"""Practical 08 - Samuel Barrett - 13038579"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def run_test():

    fancy_truck = SilverServiceTaxi("Hummer", 200, 4)
    fancy_taxi = SilverServiceTaxi("FlashCab", 200, 2)

    print(fancy_truck)
    """testing the inheritance from Car through Taxi by using .add_fuel() method here"""
    fancy_truck.add_fuel(100)
    print(fancy_truck)
    fancy_truck.drive(18)
    print(fancy_truck)

    # this should just print the fare after driving nowhere with the flagfall (tariff) already added
    print(f"${fancy_taxi.get_fare():.2f}")
    fancy_taxi.drive(18)
    # now this should calculate the total fare based on the distance driven
    print(fancy_taxi)
    print(f"${fancy_taxi.get_fare()}")


run_test()
