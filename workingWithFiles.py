import os

file_path = 'C:\\Users\\User\\Desktop\\test.txt'
folder_path = 'C:\\Users\\User\\Desktop\\textFiles'


def check_path(path):
    if os.path.exists(path):
        print('Location exists')
        if os.path.isfile(path):
            print('This is a file')
        elif os.path.isdir(path):
            print('This is a folder')
    else:
        print('Location does\'nt exist')


check_path(folder_path)
