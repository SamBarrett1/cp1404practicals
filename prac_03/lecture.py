"""
A program to ask for a user's age
"""

user_age = int(input("What is your age? "))

while user_age < 0 or user_age > 150:
    print("Invalid")
    user_age = int(input("What is your age? "))
print("You are {} years old.".format(user_age))



