"""Program to read file and convert temperatures"""
INFILE_NAME = 'temps_input.txt'
OUTFILE_NAME = 'temps_output.txt'
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius"""
# Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    in_file = open(INFILE_NAME, 'r')
    out_file = open(OUTFILE_NAME, 'w')
    # while choice != "Q":
    if choice == "C":
        for line in in_file:
            temp = float(line)
            celsius = fahrenheit_to_celsius(temp)
            print(f"{temp:19} Fahrenheit is {celsius:19} Celsius", file=out_file)
        # break
    else:
        for line in in_file:
            temp = float(line)
            fahrenheit = celsius_to_fahrenheit(temp)
            print(f"{temp:19} Celsius is {fahrenheit:19} Fahrenheit", file=out_file)
        # break
        # else:
        #     print("Invalid option")
        #     print(MENU)
        #     choice = input(">>> ").upper()
    print("Temperature conversion is ready in your output file")
    in_file.close()
    out_file.close()


def celsius_to_fahrenheit(c):
    """Convert celsius to fahrenheit"""
    fahrenheit = c * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(f):
    """Convert fahrenheit to celsius"""
    celsius = 5 / 9 * (f - 32)
    return celsius


main()

