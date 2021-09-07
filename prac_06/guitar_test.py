"""
Practical 06 - Samuel Barrett - 13038579
Guitar class test program
"""

from prac_06.guitar import Guitar


def test():
    """test program for guitar class"""

    gibson = Guitar("Gibson L-5", 1922, 16035.40)
    fender = Guitar("Fender Vintera", 1950, 1949.00)
    print("{:15} get_age()    - Expected   99. Got {:4}".format(gibson.name, gibson.get_age()))
    print("{:15} get_age()    - Expected   71. Got {:4}".format(fender.name, fender.get_age()))
    print("{:15} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))
    print("{:15} is_vintage() - Expected True. Got {}".format(fender.name, fender.is_vintage()))


test()
