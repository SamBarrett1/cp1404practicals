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

    for i in range(0, index_length):
        pos1 = indexed_name[i]
        letter1 = str(pos1)
        if letter1.isupper():
            # this nxt bit is getting the index of the (1, 'i') can't work out a better way
            # but it grabs the index of the capital letter and the capital
            the_letter = letter1[5]
            the_index = letter1[1]
            print('The Letter is : {} with index: {}'. format(the_letter, the_index))
            if int(the_index) > 1:
                previous_letter = indexed_name[int(the_index)-1]
                previous_letter_str = str(previous_letter)
                print(indexed_name[int(the_index)-1])
                if previous_letter_str.islower():
                    print('true')
                    print(filename[0:int(the_index)] + '_' + filename[int(the_index):])

        # for j in range(1, index_length):
        #     pos2 = indexed_name[j]
        #     letter2 = str(pos2)
        #     if letter1.isupper() and letter2.islower():
        #         print('True')

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


# main()

get_fixed_filename('SilentNight.txt')
