"""
CP1404
Samuel Barrett - 13038579
"""


finished = False
result = 0
while not finished:
    try:
        user_number = int(input("Enter a number: "))
        result += user_number
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)


