"""
Practical 5 - Samuel Barrett
Email dictionary program
"""


def main():
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        user_name = get_name_from_email(user_email)
        is_name = input("Is your name {}. Y/n: ".format(user_name))
        if is_name.upper() != 'Y' and is_name != "":
            is_name = input("Name: ")
        email_to_name[user_email] = is_name
        user_email = input("Email: ")
    for user_email, name in email_to_name.items():
        print("{} ({})".format(name, user_email))


def get_name_from_email(user_email):
    user_fullname = user_email.split('@')[0]
    user_names = user_fullname.split('.')
    name = " ".join(user_names).title()
    return name


main()
