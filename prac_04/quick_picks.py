"""Practical 4 - Samuel Barrett - 13038579"""

import random

ROW_NUMBER = 6
MAX_NUMBER = 45


def main():
    """Program to generate a user defined number of random quick picks"""
    user_input = int(input("How many quick picks? "))
    # Determined loop from user_input
    for i in range(0, user_input):
        # Call for a random row of different numbers
        random_row = get_random_row()
        # Nested loop to print the random row with correct formatting
        for j in range(0, ROW_NUMBER):
            print("{:2}".format(random_row[j]), end=' ')
        print()


def get_random_row():
    """Get a row of random numbers, append if new and sort"""
    random_row = []
    for j in range(0, ROW_NUMBER):
        random_number = random.randint(1, MAX_NUMBER)
        if random_number not in random_row:
            random_row.append(random_number)
        else:
            # One extra chance to not get the same random number in the list by chance
            random_number = random.randint(1, MAX_NUMBER)
            random_row.append(random_number)
    # Now the row has been filled by the loop it can be sorted
    random_row.sort()
    return random_row


main()
