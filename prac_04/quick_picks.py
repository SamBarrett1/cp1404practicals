"""Practical 4 - Samuel Barrett - 13038579"""

import random

ROW_NUMBER = 6
MAX_NUMBER = 45


def main():
    user_input = int(input("How many quick picks? "))
    for i in range(0, user_input):
        for j in range(0, ROW_NUMBER):
            random_row = get_random_row()
            print("{:2}".format(random_row[i]), end=' ')
        print()


def get_random_row():
    random_row = []
    for j in range(0, ROW_NUMBER):
        random_number = random.randint(1, MAX_NUMBER)
        random_row.append(random_number)
    random_row.sort()
    return random_row


main()
