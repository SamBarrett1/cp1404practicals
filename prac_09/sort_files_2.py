"""CP1404 Practical 9 - Samuel Barrett - 13038579"""

import shutil
import os


def main():
    """program for the user defined allocation of files to folders"""

    try:
        os.chdir('FilesToSort')
    except FileNotFoundError:
        print('File not found')

    directories = ['xlsx', 'xls', 'txt', 'png', 'jpg', 'gif', 'docx', 'doc']
    user_requests = {}

    for directory in directories:
        user_request = str(input('What category would you like to sort {} files into? '.format(directory)))
        if user_request in user_requests:
            user_requests[user_request].append(directory)
        else:
            user_requests[user_request] = [directory]

    create_directories(user_requests)
    arrange_files(user_requests)
    print('File arrangement complete')


def create_directories(dictionary):
    """Create user defined directories"""
    for key in dictionary:
        try:
            os.mkdir(key)
        except FileExistsError:
            pass
    return


def arrange_files(dictionary):
    """arrange user files into user defined directories"""
    files = []
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        files.append(filename)
    for item in dictionary.items():
        directory = item[0]
        extensions = item[1]
        for file in files:
            extension = os.path.splitext(file)[1][1:]
            if extension in extensions:
                shutil.move(file, directory + '/' + file)
    return


main()
