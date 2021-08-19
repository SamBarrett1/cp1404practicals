"""Program to read file and convert temperatures"""
INFILE_NAME = 'temps_input.txt'
OUTFILE_NAME = 'temps_output.txt'


def main():
    in_file = open(INFILE_NAME, 'r')
    out_file = open(OUTFILE_NAME, 'w')
    for line in in_file:
        temp = float(line)
        celsius = fahrenheit_to_celsius(temp)
        print(f"{temp:19} Fahrenheit is {celsius:19} Celsius", file=out_file)
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

