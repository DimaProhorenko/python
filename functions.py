# def hello(name):
#     print(f'Hello {name}')
#
#
# name = input('Enter your name')
# hello(name)


# def multiply(a, b):
#     return a * b
#
# print(multiply(6, 8))


# def greet(first_name, middle_name, last_name):
#     return f'Hello {first_name} {middle_name} {last_name}'
#
#
# print(greet(middle_name='Dude', first_name='Bro', last_name='Code'))

# num = round(abs(float(input('Enter your number'))))
# print(num)

name = 'Bro'


# def display_name():
#     name = 'Code'
#     print(name)
#
#
# print(name)
# display_name()

# def add(*nums):
#     result = 0
#     for num in nums:
#         result += num
#
#     return result
#
#
# print(add(3, 3, 5, 1, 2))


def display_full_name(**kwargs):
    msg = 'Hello '
    for value in kwargs.values():
        msg += value + ' '
    return msg

print(display_full_name(first_name='Dima', last_name='Prokhorenko'))