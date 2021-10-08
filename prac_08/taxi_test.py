"""
Practical 08 - Samuel Barrett - 13038579

A test file, this is where a main() would be defined
to write client code if it was required. To keep code
separate from the files that define the parent Classes.
This is to keep the Class files clean for reuse as modules
to be imported from.
"""

from prac_08.taxi import Taxi


def run_tests():
    """program creating new Class instances, testing the inheritance of Taxi"""

    """create a new car using the imported Taxi class as a parent"""
    user_car = Taxi("Prius1", 100)
    """using the .drive() method that is defined in the Taxi parent class"""
    user_car.drive(40)
    """printing user_car using the .__str__() method"""
    print(user_car)

    """resetting the meter with the .start_fare() method defined in Taxi"""
    user_car.start_fare()
    user_car.drive(100)
    print(user_car)

    """testing the new fare price_per_km class variable from Taxi"""
    print(f"Current fare price is: ${Taxi.price_per_km}")
    print(f"Current fare price is: ${user_car.price_per_km}")


run_tests()
