"""Practical 08 - Samuel Barrett - 13038579"""

from prac_08.car import Car
import random


class UnreliableCar(Car):
    """define a new class instance inherited from parent Car"""

    def __init__(self, name, fuel, reliability):
        """Initialise the new instance UnreliableCar, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven

