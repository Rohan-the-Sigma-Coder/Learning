import random
hangman_lives = 0
random_foods = ['pizza', 'pasta', 'burger', 'fries', 'cake', 'pie']
random_food = random.choice(random_foods)
random_food_list = list(random_food)
output_list = ['_'] * len(random_food_list)
actual_output_list = []
print('_ ' * len(random_food))
while True:
    user_guess = input('Enter a letter: ')
    if len(user_guess) == 1 and user_guess is not int:
        for i in range(len(random_food_list)):
            if user_guess == random_food_list[i]:
                output_list[i] = user_guess
        if user_guess not in random_food_list:
            hangman_lives += 1
            print('😡' * hangman_lives)
            if hangman_lives == 3:
                print(f'You lost! The word was {random_food}!')
                quit()
        print(' '.join(output_list))
        if '_' not in output_list:
            print('You guessed the word!')
            break

    else:
        print('Invalid input')
        break
    

