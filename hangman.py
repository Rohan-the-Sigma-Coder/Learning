import random
output_list = []
random_foods = ['pizza', 'pasta', 'burger', 'fries', 'cake', 'pie']
random_food = random.choice(random_foods)
random_food_list = list(random_food)
print('_' * len(random_food))
while True:
    user_guess = input('Enter a letter: ')
    if len(user_guess) == 1 and user_guess is not int:
        for i in range(len(random_food_list)):
            if user_guess == random_food_list[i]:
                output_list.append(user_guess)
            else:
                output_list.append('_')
            print(*output_list)
    

