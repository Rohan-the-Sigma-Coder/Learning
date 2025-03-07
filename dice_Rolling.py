import random

def die_rolling():
    die_rolls = 0
    while True:
        user_input = input('Roll the dice? (y/n): ').lower()
        if user_input == 'y':
            die_rolls += 1
            die_counter = int(input('How many dices do you want to roll: '))
            die_list = []
            for i in range(die_counter):
                die_list.append(random.randint(1, 6))
            print(die_list)
        elif user_input == 'n':
            print(f'Thanks for playing! You rolled {die_rolls} times.')
            break
        elif ValueError:
            print('Invalid choice!')


die_rolling()