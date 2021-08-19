"""
Program to read file and convert temperatures

Dependencies: This program relies on temps_input.py
to create and populate it's in_file 'temps_input.txt'
"""

INFILE_NAME = 'temps_input.txt'
OUTFILE_NAME = 'temps_output.txt'
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius"""


def main():
    """Read file and convert to celsius or fahrenheit"""
    print(MENU)
    choice = input(">>> ").upper()
    # Open the input and output files
    in_file = open(INFILE_NAME, 'r')
    out_file = open(OUTFILE_NAME, 'w')
    if choice == "C":
        for line in in_file:
            temp = float(line)
            celsius = fahrenheit_to_celsius(temp)
            print(f"{temp:19} Fahrenheit is {celsius:19} Celsius", file=out_file)
    else:
        for line in in_file:
            temp = float(line)
            fahrenheit = celsius_to_fahrenheit(temp)
            print(f"{temp:19} Celsius is {fahrenheit:19} Fahrenheit", file=out_file)
    print("Temperature conversion is ready in your output file")
    # Close the input and output files
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

