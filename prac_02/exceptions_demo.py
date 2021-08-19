"""
CP1404
Samuel Barrett - 13038579
"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


"""
Prac Question Answers:
1) There will be an ValueError if you type a letter
2) There will be a ZeroDivision Error if use type a zero for the denominator
3) Add an input filter that asks the user to retype their input if it is zero
"""

