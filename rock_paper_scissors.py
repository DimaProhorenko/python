import random


def get_winner(player, ai):
    if (player + 1) % 3 == ai:
        return 'AI has won'
    elif player == ai:
        return 'It\'s a draw'
    else:
        return 'Player has won'


def display_result(player, ai, result):
    print(
        f'You chose {choices[player]}, ai chose {choices[ai]}...\n{result}')


def get_user_input():
    return int(input('Enter 1 - rock, 2 - paper, 3 - scissors: ')) - 1

def get_ai_choice():
    return random.randint(0, 2)


def play():
    user_choice = -1
    while user_choice < 0 or user_choice > 2:
        try:
            user_choice = get_user_input()

            if user_choice < 0 or user_choice > 2:
                raise ValueError

            comp_choice = get_ai_choice()
            result = get_winner(user_choice, comp_choice)
            display_result(user_choice, comp_choice, result)
        except ValueError:
            print('Only numbers between 1 and 3 are available')


choices = ['rock', 'paper', 'scissors']

while True:
    play()
    playAgain = int(input('Type 1 to play again, 0 to quit: '))

    if playAgain != 1:
        break


print('Thanks for playing... Have a nice day')

