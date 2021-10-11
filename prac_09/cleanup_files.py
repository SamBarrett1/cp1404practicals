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


def get_fixed_filename(new_name):
    """Return a 'fixed' version of filename."""
    new_name = new_name.replace(" ", "_").replace(".TXT", ".txt")
    indexed_name = []
    print('Before any formatting')
    print(new_name)

    for char in enumerate(new_name):
        indexed_name.append(char)
    index_length = len(indexed_name)

    modified_filename = new_name
    underscore = 0

    # First formatting check looking for capital letters without underscores
    for i in range(0, index_length):
        pos = indexed_name[i]
        letter = pos[1]
        if letter.isupper():
            # if the letter is uppercase make character to the left '_' if it's not at front of the filename
            # print('The Letter is : {} with index: {}'.format(letter, pos[0]))
            if int(pos[0]) > 1:
                index_start = int(pos[0]) + underscore
                index = int(pos[0])
                # print('This is Index with underscore: {} and type: {}'.format(index, type(index)))
                modified_filename = (modified_filename[0:index_start] + '_' + new_name[index:])
                # print(modified_filename)
                # print('....................next loop')
                underscore += 1
        else:
            pass

    # Start of the next formatting check for lowercase letters next to '_'
    print('After first loop of checks')
    print(modified_filename)
    new_indexed_name = []

    # Needing the modified_filename here if the first formatting check needed to make any changes
    for char in enumerate(modified_filename):
        new_indexed_name.append(char)
    # print(new_indexed_name)
    new_index_length = len(new_indexed_name)

    # split modified_filename into a list of characters
    new_list_of_characters = []
    for char in modified_filename:
        new_list_of_characters.append(char)
    # print(new_list_of_characters)

    # loop through the ascii codes to find
    for i in range(0, new_index_length):
        pos = new_indexed_name[i]
        letter = pos[1]
        underscore_ascii_code = ord(letter)

        # Only proceed to check what's next where an '_' is located
        if underscore_ascii_code == 95:
            # get index of next enumerated character tuple eg: (0, 'S') pos[0] = 0 and pos[1] = 'S'
            next_pos = int(pos[0]) + 1
            next_letter_tuple = new_indexed_name[next_pos]
            next_letter = next_letter_tuple[1]
            # print('this is next letter tuple: {}'.format(next_letter_tuple))
            # print('this is next_pos index: {}'.format(next_pos))
            # print('this is next_letter: {}'.format(next_letter))
            # Only proceed if the next letter is lowercase
            if next_letter.islower():
                make_upper = next_letter
                title_case = make_upper.title()
                # print('this is title case: {}'.format(title_case))
                # print('changed to Uppercase successfully')
                if int(pos[0]) > 1:
                    new_list_of_characters[next_pos] = title_case
                    modified_filename = ''.join(new_list_of_characters)
                    # print(modified_filename)
        else:
            pass

    print('After second loop of checks')
    print(modified_filename)

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


main()

# get_fixed_filename('SilentNight_tonightWith_lucidAwareness.txt')
