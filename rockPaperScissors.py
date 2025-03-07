import random
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
rps_dictionary = {
ROCK: '🪨',
SCISSORS: '✂',
PAPER: '📃'
}
choices = tuple(rps_dictionary.keys())
def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice')


def display_choices(user_choice, computer_choice):
    print(f'You chose {rps_dictionary[user_choice]}')
    print(f'Computer chose {rps_dictionary[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif user_choice == ROCK and computer_choice == SCISSORS:
        print('You win!')
    elif user_choice == PAPER and computer_choice == ROCK:
        print('You win!')
    elif user_choice == SCISSORS and computer_choice == PAPER:
        print('You win!')
    else:
        print('You lose!')


def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)
        user_input = input('Do you want to continue? (y/n): ')
        if user_input == 'y':
            continue
        elif user_input == 'n':
            print('Thanks for playing')
            quit()
        else:
            print('Invalid Choice')


play_game()









