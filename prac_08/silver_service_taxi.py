"""Practical 08 - Samuel Barrett - 13038579"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """define a new class instance inherited from parent Taxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise the new instance SilverServiceTaxi, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km
        self.fanciness = fanciness * self.price_per_km

    def __str__(self):
        return "{}, {}km on current fare, ${:.2f}/km " \
               "plus flagfall of ${:.2f}, total fare is ${:.2f}".format(super().__str__(),
                                                                        self.current_fare_distance,
                                                                        self.fanciness,
                                                                        self.flagfall,
                                                                        self.get_fare())

    def get_fare(self):
        """Return the price for the taxi trip."""
        fancy_fare = self.price_per_km * self.current_fare_distance + self.flagfall
        return fancy_fare


