


try:
    numerator = int(input('Enter a number to divide: '))
    divider = int(input('Enter a number to divide by: '))
    result = numerator / divider
    print(result)
except ZeroDivisionError:
    print('Cannot divide by zero')
except ValueError as e:
    print('Value is not a number')
    print(e)