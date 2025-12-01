print('''Welcome to the Python Multitasker! Enter the number corresponding to the activity you desire to execute!
1 --- Word Replacement
2 --- Average Calculator
3 --- Random Name Generator
4 --- Random Number Generator
5 --- Calculator (for two integers only)
6 --- Factorial Calculator
7 --- Even or Odd
8 --- Least or Greatest Number Calculator
9 --- Subject, Verb, and Noun Sentence Former
10 --- Multiples Calculator
11 --- Upper or Lowercase Converter
12 --- Coin Toss
13 --- Character Counter''')
activity_number = input('Enter activity number: ')
activity_number = int(activity_number)
def word_replacement():
    sentence = input('Enter a sentence: ')
    from_word = input('Enter a word or phrase in that sentence to replace: ')
    to_word = input('Enter a word or phrase to replace your original word: ')
    new_sentence = sentence.replace(from_word, to_word)
    print('Your new sentence is: ', new_sentence)
    activity_number = input('Enter activity number: ')
    activity_number = int(activity_number)
    if activity_number == 1:
        word_replacement()
    elif activity_number == 2:
        average_calculator()
    elif activity_number == 3:
        random_name_generator()


def average_calculator():
    amount_of_numbers = int(input('How many numbers do you want to find the average of? : '))
    while amount_of_numbers <= 1:
        print("ERROR! INVALID NUMBER HAS BEEN ENTERED, PLEASE REENTER NUMBER YOU AUTISTIC MONKEY!")
        amount_of_numbers = int(input('How many numbers do you want to find the average of? : '))
    adder = 0
    numbers = 0
    for x in range(amount_of_numbers):
        numbers = float(input('Enter a number: '))
        adder += numbers
    answer = adder / amount_of_numbers
    new_answer = (format(answer, ".2f"))
    print('The average of the numbers is approximately: ', new_answer)
    activity_number = input('Enter activity number: ')
    activity_number = int(activity_number)
    if activity_number == 1:
        word_replacement()
    elif activity_number == 2:
        average_calculator()
    elif activity_number == 3:
        random_name_generator()


def random_name_generator():
    import random
    array_name_list = []
    amount_of_names = int(input('How many names do you want to generate out of?: '))
    for x in range(amount_of_names):
        name_counter = input('Enter name: ')
        name_counter = str(name_counter)
        array_name_list.insert(1, name_counter)
    amount_random_names = amount_of_names - 1
    random_name = random.randint(0, amount_random_names)
    import time
    interval_time_name = 3
    print('Generating random name out of your list in...')
    for y in range(3):
        print(interval_time_name)
        interval_time_name -= 1
        time.sleep(1)
    print(array_name_list[random_name])
    activity_number = input('Enter activity number: ')
    activity_number = int(activity_number)
    if activity_number == 1:
        word_replacement()
    elif activity_number == 2:
        average_calculator()
    elif activity_number == 3:
        random_name_generator()



def random_number_generator():
    import random
    array_number_list = []
    amount_of_numbers = input('How many numbers do you want to generate out of?: ')
    amount_of_numbers = int(amount_of_numbers)
    for x in range(amount_of_numbers):
        numbers = float(input('Enter number: '))
        array_number_list.insert(1, numbers)
    amount_random_number = amount_of_numbers - 1
    random_number = random.randint(0, amount_random_number)
    import time
    interval_time_number = 3
    print('Generating random number out of your list in...')
    for i in range(3):
        print(interval_time_number)
        interval_time_number -= 1
        time.sleep(1)
    final_number = array_number_list[random_number]
    print('Random number: ', final_number)
    activity_number = input('Enter activity number: ')
    activity_number = int(activity_number)
    if activity_number == 1:
        word_replacement()
    elif activity_number == 2:
        average_calculator()
    elif activity_number == 3:
        random_name_generator()
    elif activity_number == 4:
        random_number_generator()
    elif activity_number == 5:
        calculator()


def calculator():
    first_integer = input('Enter first integer: ')
    first_integer = float(first_integer)
    second_integer = input('Enter second integer: ')
    second_integer = float(second_integer)
    operation = input('''Which operation do you wanna use between operators?:
    Type M for multiplication
    Type D for division
    Type A for addition
    Type S for subtraction
    ...... ---> ''')
    operation = operation.upper()
    if operation == 'M':
        answer = first_integer * second_integer
        actual_answer = format(answer, ".2f")
        print('Your answer is: ', actual_answer)
        activity_number = input('Enter activity number: ')
        activity_number = int(activity_number)
        if activity_number == 1:
            word_replacement()
        elif activity_number == 2:
            average_calculator()
        elif activity_number == 3:
            random_name_generator()
        elif activity_number == 4:
            random_number_generator()
        elif activity_number == 5:
            calculator()
    if operation == 'D':
        if second_integer == 0:
            print('UNDEFINED (Second integer is 0)')
        else:
            answer = first_integer / second_integer
            actual_answer = format(answer, ".2f")
            print('Your answer is: ', actual_answer)
        activity_number = input('Enter activity number: ')
        activity_number = int(activity_number)
        if activity_number == 1:
            word_replacement()
        elif activity_number == 2:
            average_calculator()
        elif activity_number == 3:
            random_name_generator()
        elif activity_number == 4:
            random_number_generator()
        elif activity_number == 5:
            calculator()

    if operation == 'A':
        answer = first_integer + second_integer
        actual_answer = format(answer, ".2f")
        print('Your answer is: ', actual_answer)
        activity_number = input('Enter activity number: ')
        activity_number = int(activity_number)
        if activity_number == 1:
            word_replacement()
        elif activity_number == 2:
            average_calculator()
        elif activity_number == 3:
            random_name_generator()
        elif activity_number == 4:
            random_number_generator()
        elif activity_number == 5:
            calculator()
    if operation == 'S':
        answer = first_integer - second_integer
        actual_answer = format(answer, ".2f")
        print('Your answer is: ', actual_answer)
        activity_number = input('Enter activity number: ')
        activity_number = int(activity_number)
        if activity_number == 1:
            word_replacement()
        elif activity_number == 2:
            average_calculator()
        elif activity_number == 3:
            random_name_generator()
        elif activity_number == 4:
            random_number_generator()
        elif activity_number == 5:
            calculator()


def factorial_calculator():
    asker = input('Enter a number I will show you the factorial for that number: ')
    asker = int(asker)
    factorial = 1
    for i in range(asker, 0, -1):
        factorial *= i
    print('FACTORIAL : ', factorial)


def even_or_odd():
    input_number = int(input('Enter a number, and I will show you if it is even or odd: '))
    print('It is ' + 'even' if input_number % 2 == 0 else 'odd')

def least_greatest():
    user_input1 = input('Enter a number: ')
    user_input1 = int(user_input1)
    user_input2 = input('Enter a number: ')
    user_input2 = int(user_input2)
    if user_input1 == user_input2:
        print("It's the same number stupid, run the program again ...>")
        import sys
        sys.exit()
    least_or_greatest = input(' Type L if you want to find least number or G if you want to find greater number: ')
    if least_or_greatest == 'L':
        print('The least number is', user_input1 if user_input1 < user_input2 else user_input2)
    else:
        print('The greater number is', user_input1 if user_input1 > user_input2 else user_input2)


def sentence_former():
    subject = input('Subject: ')
    verb = input('Verb (present tense): ')
    noun = input('Noun: ')
    time_wait = 3
    import time
    print('Sentence forming in...')
    for i in range (3):
        print(time_wait)
        time_wait -= 1
        time.sleep(1)
    print('Random Sentence: ', subject, verb +'ed', noun)


def multiples_calculator():
    num = int(input('Enter a number and I will show you the first 10 multiples for that number:'))
    print('Multiples will generate one after the other with half second intervals')
    import time
    num_array = []
    array = 0
    for i in range(num, num * 10 + 1, num):
        num_array.insert(9, i)
    for i in range(10):
        print(num_array[array])
        time.sleep(.5)
        array += 1
    print('DONE')


def upper_lower_case():
    word_phrase = input('Enter a word or phrase to convert: ')
    upper_or_lower = input('Do you want to convert to upper(Type U) or lower case(Type L)?')
    upper_or_lower = upper_or_lower.upper()
    if upper_or_lower == 'U':
        new_word_phrase = word_phrase.upper()
        print('Your new word or sentence will be displayed in...')
        time_num = 3
        import time
        for i in range(3):
            print(time_num)
            time_num -= 1
            time.sleep(1)
        print(new_word_phrase)
    if upper_or_lower == 'L':
        new_word_phrase = word_phrase.lower()
        print('Your new word or sentence will be displayed in...')
        time_num = 3
        import time
        for i in range(3):
            print(time_num)
            time_num -= 1
            time.sleep(1)
        print(new_word_phrase)


def coin_toss():
    import random
    coin = input("Type 'FLIP' to flip the coin: ")
    coin = coin.upper()
    if coin == 'FLIP':
        rand = random.randint(0,1)
        if rand == 0:
            print('HEADS')
        else:
            print('TAILS')


def character_counter():
    phrase = input('Enter a phrase and I will show you how many characters are in the phrase (including spaces): ')
    countdown = 3
    import time
    for i in range(3):
        print(countdown)
        countdown -= 1
        time.sleep(1)
    print('The number of characters in your phrase is', len(phrase))
if activity_number == 1:
    word_replacement()
elif activity_number == 2:
    average_calculator()
elif activity_number == 3:
    random_name_generator()
elif activity_number == 4:
    random_number_generator()
elif activity_number == 5:
    calculator()
elif activity_number == 6:
    factorial_calculator()
elif activity_number == 7:
    even_or_odd()
elif activity_number == 8:
    least_greatest()
elif activity_number == 9:
    sentence_former()
elif activity_number == 10:
    multiples_calculator()
elif activity_number == 11:
    upper_lower_case()
elif activity_number == 12:
    coin_toss()
elif activity_number == 13:
    character_counter()