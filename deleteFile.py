import os
import shutil

file_path = 'C:\\Users\\User\\Desktop\\test.txt'
empty_folder_path = 'C:\\Users\\User\\Desktop\\empty_folder'
text_folder_path = 'C:\\Users\\User\\Desktop\\textFiles'

try:
    # os.remove(empty_folder_path)
    # os.rmdir(text_folder_path)
    shutil.rmtree(text_folder_path)
except FileNotFoundError:
    print(empty_folder_path + ' was not found')
except PermissionError:
    print('You do not have a permission to delete that')
except OSError:
    print('You cannot delete this')
else:
    print('File was deleted')