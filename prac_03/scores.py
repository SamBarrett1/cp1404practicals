"""Practical 03 extension - Samuel Barrett - 13038579"""


import random


def main():
    """Program to print random results to a file"""
    user_scores = int(input("How many random scores? "))
    out_file = open("random_results.txt", 'w')
    for i in range(0, user_scores):
        random_grade = get_random_grade()
        random_result = get_result(random_grade)
        print(f"{random_grade:2} is {random_result}", file=out_file)
    out_file.close()


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
    """generate a random grade"""
    random_grade = random.randint(0, 100)
    return random_grade


main()

