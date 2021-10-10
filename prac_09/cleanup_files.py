"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Universalise txt format of filenames"""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # loop through the tuple of filenames created by os.walk()
        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)
            spacing = get_spacing()
            print('Renaming {:{}} to {}'.format(full_name, spacing, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    indexed_name = []
    for char in enumerate(filename):
        indexed_name.append(char)
    print(indexed_name)
    index_length = len(indexed_name)

    for i in range(0, index_length):
        pos1 = indexed_name[i]
        pos2 = indexed_name[i+1]
        print('This is pos1: {} and pos2: {}'.format(pos1, pos2))

    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def get_spacing():
    """get length of longest directory + filename for print spacing"""
    longest_str = 0
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            str_length = len(full_name)
            if str_length > longest_str:
                longest_str = str_length
    return longest_str


main()
