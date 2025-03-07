import random
attempts = 0
attempts_limit = 10
minimum_value = int(input('Minimum value for range: '))
maximum_value = int(input('Maximum value for range: '))
secret_number = random.randint(minimum_value, maximum_value)
while True:
    attempts += 1
    if attempts == attempts_limit:
        print(f'You lose! The secret number was {secret_number}')
        break
    user_number = int(input(f'Guess the number between {minimum_value} and {maximum_value}: '))
    if secret_number > user_number:
        print('Too Low!')
    elif secret_number < user_number:
        print('Too High!')
    elif secret_number == user_number:
        print('Congratulations! You guessed the number!')
        break
    else:
        print('Please enter a valid number')