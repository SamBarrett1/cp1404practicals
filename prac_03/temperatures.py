"""
CP1404/CP5632 - Practical
Samuel Barrett - 13038579

Pseudocode for temperature conversion:

menu = C - Convert Celsius to Fahrenheit
       F - Convert Fahrenheit to Celsius
       Q - Quit
display menu
choice = get user request from menu
while choice != "Q"
    if choice == "C"
        celsius = get as float from user input
        fahrenheit = celsius * 9.0 / 5 + 32
        display fahrenheit to 2 decimal places
    else if choice == "F"
        fahrenheit = get as float from user input
        celsius = 5 / 9 * (fahrenheit - 32)
        display celsius to 2 decimal places
    else
        display "Invalid option"
    display menu
    choice = get user request from menu
display "Thank-you"

"""


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Temperature conversion program"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(c):
    """Convert celsius to fahrenheit"""
    fahrenheit = c * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(f):
    """Convert fahrenheit to celsius"""
    celsius = 5 / 9 * (f - 32)
    return celsius


main()

