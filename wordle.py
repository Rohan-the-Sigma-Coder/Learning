import random
def wordle():    
    loop_num = 0
    feedback = []
    word_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    random_word = []
    for i in range(5):
        random_word.append(random.choice(word_list))
    user_guess = input('Guess 5-letter word(just random letters): ')
    if len(user_guess) != 5:
        print('Invalid response')
        quit()
    user_guess = list(user_guess)
    for char in user_guess:
        letter = user_guess[loop_num]
        random_word_letter = random_word[loop_num]
        if letter in random_word:
            if letter == random_word_letter:
                feedback.append('🟢')
            else:
                feedback.append('🟡')
        else:
            feedback.append('🔴')
        loop_num += 1
    print(*feedback + random_word)


def wordle_num():
    loop_num = 0
    num_feedback = []
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random_num = []
    for i in range(5):
        random_num.append(random.choice(num_list))
    user_guess = input('Guess 5-character number: ')
    if len(user_guess) != 5:
        print('Invalid response')
        quit()
    user_guess = list(user_guess)
    for number in user_guess:
        num = user_guess[loop_num]
        random_num_char = random_num[loop_num]
        if num in random_num:
            if num == random_num_char:
                num_feedback.append('🟢')
            else:
                num_feedback.append('🟡')
        else:
            num_feedback.append('🔴')
        loop_num += 1
    print(*num_feedback)



wordle()