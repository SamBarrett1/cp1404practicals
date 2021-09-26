"""Practical 08 - Samuel Barrett - 13038579"""

from prac_08.taxi import Taxi


def run_tests():

    user_car = Taxi("Prius1", 100, 1.23)
    user_car.drive(40)
    print(user_car)

    user_car.start_fare()
    user_car.drive(100)
    print(user_car)


run_tests()
