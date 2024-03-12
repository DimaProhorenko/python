import random

x = random.randint(0, 100)
y = random.random()
my_list = ['rock', 'paper', 'scissors']

# choise = random.choice(my_list)
random.shuffle(my_list)
print(my_list)