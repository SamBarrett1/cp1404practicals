"""program to create text file with temps"""
import random
FILENAME = 'temps_input.txt'
TOTAL_TEMPS = 15


def main():
    """create temps file with random temps"""
    out_file = open(FILENAME, 'w')
    for i in range(0, TOTAL_TEMPS):
        random_front = random.randint(-200, 200)
        random_back = random.randint(000000000000000, 999999999999999)
        print(f"{random_front}.{random_back}", file=out_file)
    out_file.close()


main()

