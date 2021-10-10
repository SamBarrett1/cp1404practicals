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
    count = 0
    indexed_name = []
    print(filename)
    for char in enumerate(filename):
        indexed_name.append(char)
    print(indexed_name)
    index_length = len(indexed_name)
    print('This is the index_length: {}:'.format(index_length))

    # function to return count of uppercase letters
    upper_case_count = get_upper_count(filename)
    print('Uppercase cnt: {}'.format(upper_case_count))

    modified_filename = filename
    underscore = 0

    for i in range(0, index_length):
        pos1 = indexed_name[i]
        letter1 = pos1[1]
        if letter1.isupper():
            # print('The Letter is : {} with index: {}'.format(letter1, pos1[0]))
            if int(pos1[0]) > 1:
                index_start = int(pos1[0]) + underscore
                index = int(pos1[0])
                # print('This is Index with underscore: {} and type: {}'.format(index, type(index)))
                modified_filename = (modified_filename[0:index_start] + '_' + filename[index:])
                print(modified_filename)
                underscore += 1
                print(underscore)

    return modified_filename


def get_upper_count(filename):
    """get the count of uppercase letters in the filename"""
    count = 0
    indexed_name = []
    for char in enumerate(filename):
        indexed_name.append(char)
    for i in range(0, len(indexed_name)):
        pos1 = indexed_name[i]
        letter1 = str(pos1)
        if letter1.isupper():
            count += 1
    return count


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


# main()

get_fixed_filename('SilentNightTonightWithStars.txt')
