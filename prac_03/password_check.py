"""A program to get a password"""


PASSWORD_LENGTH = 8


def main():
    """Main function"""
    user_password = get_password()
    print_asterix(user_password)


def get_password():
    """Get a user password"""
    user_password = input("Enter your new password: ")
    while len(user_password) < PASSWORD_LENGTH:
        print("Invalid: password must be {} characters long".format(PASSWORD_LENGTH))
        user_password = input("Enter your new password: ")
    return user_password


def print_asterix(password_string):
    """Print password as asterix string"""
    for i in range(len(password_string)):
        print("*", end='')


main()

