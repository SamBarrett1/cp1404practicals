"""CP1404 Practical 9 - Samuel Barrett - 13038579"""

import shutil
import os


def main():
    """sort common files into folders created with their extension names"""
    print("Starting directory is: {}".format(os.getcwd()))
    try:
        os.chdir('FilesToSort')
    except FileNotFoundError:
        print('File not found')

    directories = ['xlsx', 'xls', 'txt', 'png', 'jpg', 'gif', 'docx', 'doc']

    for directory in directories:
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass

    # start looping through directory names
    for i in directories:
        directory = i
        try:
            os.chdir('FilesToSort')
        except FileNotFoundError:
            pass
        common_files = common_file_types(directory)
        for file in common_files:
            shutil.move(file, directory + '/' + file)
        try:
            os.chdir('..')
        except FileNotFoundError:
            pass


def common_file_types(folder):
    """get a list of common file types based on directory name"""
    files = []
    same_extensions = []
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        files.append(filename)
    for file in files:
        # get the file extension with [1] with the '.' sliced off with [1:]
        extension = os.path.splitext(file)[1][1:]
        if extension == folder:
            same_extensions.append(file)
    return same_extensions


def run_tests():
    """run tests with test directory"""
    direct = 'xlsx'
    common_files = common_file_types(direct)
    print(common_files)


# run_test()


main()
