"""
Practical 06 - Samuel Barrett - 13038579
User Guitar listing with class
"""

from prac_06.guitar import Guitar


def main():
    """Program to manage a guitar collection"""

    guitar_names = []
    guitar_total = int(input("How many guitars do you want to list: "))
    for i in range(0, guitar_total):
        guitar_name = input("Name: ")
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        guitar_info = Guitar(guitar_name, guitar_year, guitar_cost)
        guitar_names.append(guitar_info)

    print("My guitars!")
    for obj in guitar_names:
        print(f"Name: {obj.name}")
        print(f"Year: {obj.year}")
        print(f"Cost: {obj.cost}")
        print(f"{obj.name} ({obj.year}) : ${obj.cost} added.")

    # some inspiration was needed for the following code after quite some effort
    if guitar_names:
        print("These are my guitars:")
        for i, guitar in enumerate(guitar_names):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>10} ({1.year}), worth ${1.cost:5,.2f}\
                 {2}".format(i + 1, guitar, vintage_string))
    else:
        print("You should buy a guitar")


main()

