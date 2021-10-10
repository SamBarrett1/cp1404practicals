"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory, with error handling
    try:
        os.chdir('Lyrics/Christmas')
    except FileNotFoundError:
        print('File not found')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory, with error handling
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # My tests change into temp, to get files back to ../Christmas
    # os.chdir("temp")
    # print("Directory is now: {}".format(os.getcwd()))

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):

        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        shutil.move(filename, 'temp/' + new_name)

        # My line to get the files back from 'temp' to ../Christmas
        # shutil.move(filename, '../Christmas' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
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


# demo_walk()
