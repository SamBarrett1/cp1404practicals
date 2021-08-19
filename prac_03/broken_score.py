"""
CP1404/CP5632 - Practical
Samuel Barrett - 13038579

Broken program to determine score status
"""

import random


def main():
    """Program to return result of grades"""
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)
    # calling part c) the random grade function
    random_grade = get_random_grade()
    random_result = get_result(random_grade)
    print("Random grade of {} will be {}".format(random_grade, random_result))


def get_result(grade):
    """get result of grade"""
    if grade < 0 or grade > 100:
        return "Invalid score"
    elif grade >= 90:
        return "Excellent"
    elif grade >= 50:
        return "Passable"
    else:
        return "Bad"


def get_random_grade():
    random_grade = random.randint(0, 100)
    return random_grade


main()

