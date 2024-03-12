import os

file_name = 'move.txt'
src_path = 'C:\\Users\\User\\Desktop\\' + file_name
destination_path = 'C:\\Users\\User\\Desktop\\textFiles\\' + file_name

try:
    if os.path.exists(destination_path + file_name):
        print('File already exists')
    else:
        os.replace(src_path, destination_path)
        print(src_path + ' was moved')
except FileNotFoundError:
    print(src_path + ' was not found')