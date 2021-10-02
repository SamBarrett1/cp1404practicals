"""Practical 08 - Samuel Barrett - 13038579"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def run_test():

    fancy_taxi = SilverServiceTaxi("FlashCab", 200, 2)

    fancy_taxi.drive(18)

    print(fancy_taxi)
    print(fancy_taxi.get_fare())


run_test()

