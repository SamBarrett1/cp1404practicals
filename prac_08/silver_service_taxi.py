"""Practical 08 - Samuel Barrett - 13038579"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """define a new class instance inherited from parent Taxi which is already a sub-class (child) of Car"""
    # this is a class only variable
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise the new instance SilverServiceTaxi, based on parent class Taxi."""
        super().__init__(name, fuel)
        # bring a new attribute in like this by referring to the extra parameter added to __init__()
        self.fanciness = fanciness
        # .price_per_km comes in from Taxi's class variable, and it can be modified in this class only in __inti__()
        # remember this is the same as self.price_per_km = self.price_per_km * fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """define print string with an override to include Taxi string, and add extras"""
        # you only need one {} for an override, it will include all of the {}'s in super.__str__() in that {}
        return "{} with fanciness, plus flagfall of ${:.2f}, total fare is ${:.2f}".format(super().__str__(),
                                                                                           self.flagfall,
                                                                                           self.get_fare())

    def get_fare(self):
        """Return the price for the fancy taxi trip."""
        # the next 2 lines work as well, but the code in use on the last line is cleaner
        # fancy_cab_fare = super().get_fare() + self.flagfall
        # return fancy_cab_fare
        return super().get_fare() + self.flagfall
