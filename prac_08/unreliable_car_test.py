"""Practical 08 - Samuel Barrett - 13038579"""

from prac_08.unreliable_car import UnreliableCar


def run_tests():

    good_car = UnreliableCar("Good Car", 100, 90)
    bad_car = UnreliableCar("Bad Car", 100, 10)

    for i in range(1, 15):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    """print the final states of the cars"""
    print(good_car)
    print(bad_car)


run_tests()
