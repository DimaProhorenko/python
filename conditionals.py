age = int(input('Enter your age: '))

if age >= 18:
    print('You are allowed to vote')
elif age <= 0:
    print('You haven\'n been born yet')
else:
    print('You are not allowed to vote')
