import random
def random_generator():
    print(random.randint(0, 52))


deck_list = []
def cards_random():
    suite_num = 0
    card_num = 2
    card_value = ''
    if suite_num == 0:
        suite = 'Spades'
    elif suite_num == 1:
        suite = 'Hearts'
    elif suite_num == 2:
        suite = 'Cloves'
    elif suite_num == 3:
        suite = 'Clover'
    for i in range(4):
        for i in range(9):
            deck_list.append(suite + '-' + str(card_num))
            card_num += 1
        for x in range(4):
            if card_num == 11:
                card_value = 'Jack'
            elif card_num == 12:
                card_value = 'Queen'
            elif card_num == 13:
                card_value = 'King'
            elif card_num == 14:
                card_value = 'Aces'
            deck_list.append(suite + '-' + str(card_value))
            card_num += 1
        card_num = 2
        suite_num += 1
        if suite_num == 0:
            suite = 'Spades'
        elif suite_num == 1:
            suite = 'Hearts'
        elif suite_num == 2:
            suite = 'Cloves'
        elif suite_num == 3:
            suite = 'Clover'
    print(*deck_list)
    for i in range(26):
        card_1 = random.randint(0,51)
        card_2 = random.randint(0,51)
        card_1_value = deck_list[card_1]
        deck_list.remove(str(card_1_value))
        card_2_value = deck_list[card_2]
        deck_list.remove(str(card_2_value))
        deck_list.insert(card_2, card_1_value)
        deck_list.insert(card_1, card_2_value)
    print(*deck_list)




    # for i in range(1000):
    #     random_card = random.randint(0, 51)
    #     print(deck_list[random_card])

cards_random()