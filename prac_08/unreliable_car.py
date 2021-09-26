"""Practical 08 - Samuel Barrett - 13038579"""

from prac_08.car import Car


class UnreliableCar(Car):
    """define a new class instance inherited from parent Car"""

    def __init__(self, name, fuel, reliability):
        """Initialise the new instance UnreliableCar, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        distance_driven = super().drive(distance)
        if self.reliability > distance_driven:
            return distance_driven
        else:
            return "Car not reliable enough to make it"

