"""
Samuel Barrett - 13038579
"""

NUMBERS = 5


def main():
    user_numbers = []
    user_number_total = 0
    for i in range(1, NUMBERS + 1):
        user_number = int(input('Number: '))
        user_numbers.append(user_number)
        user_number_total += user_number
    print("The first number is {}".format(user_numbers[0]))
    print("The last number is {}".format(user_numbers[-1]))
    print("The smallest number is {}".format(min(user_numbers)))
    print("The largest number is {}".format(max(user_numbers)))
    print("The average of the numbers is {:.1f}".format(user_number_total/NUMBERS))


main()
