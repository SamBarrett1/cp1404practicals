"""
Practical 06 - Samuel Barrett - 13038579
Guitar class program
"""

CURRENT_YEAR = 2021
VINTAGE_AGE = 50


class Guitar:
    """Guitar class object"""

    def __init__(self, name="", year=0, cost=0):
        """guitar class constructor"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """print __str__ method"""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """get guitar age"""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """get vintage status"""
        # current_year = 2021
        # guitar_year = self.get_age()
        # if current_year - guitar_year > 50:
        #     return True
        # else:
        #     return False
        return self.get_age() >= VINTAGE_AGE




