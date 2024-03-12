file_path = 'C:\\Users\\User\\Desktop\\test.txt'

# Read A File
# try:
#     with open(file_path) as file:
#         print(file.read())
# except FileNotFoundError:
#     print('File was not found')

# Write To a File
# try:
#     with open(file_path, 'w') as file:
#         file.write('Yooooooooou\nThis is some text\nHave a good one\n')
# except FileNotFoundError:
#     print('File was not found')


# Append to a file
try:
    with open(file_path, 'a') as file:
        file.write('Have a nice day')
except FileNotFoundError:
    print("File was not found")