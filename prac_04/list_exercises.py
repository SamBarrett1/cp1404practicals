"""
Samuel Barrett - 13038579
"""

NUMBERS = 5


def main():
    user_name = input("What is your name: ")
    access_token = check_user_access(user_name)
    if access_token:
        print("Access granted")
    else:
        print("Access denied")
        return
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
    print("The average of the numbers is {:.1f}".format(user_number_total / NUMBERS))
    print("The average of the numbers is {:.1f}".format(sum(user_numbers) / NUMBERS))


def check_user_access(name_string):
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    return name_string in usernames


main()
