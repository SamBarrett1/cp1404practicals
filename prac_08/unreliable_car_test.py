"""Practical 08 - Samuel Barrett - 13038579"""

from prac_08.unreliable_car import UnreliableCar
import random


def run_tests():
    random_number = random.randint(0, 100)
    reliability = float(random_number)

    user_car = UnreliableCar("UnreliableCar", 100, reliability)
    user_car.drive(90)
    print(user_car)


run_tests()
