def even_sorter():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    new_list = []
    for i in range(22):
        if i % 2 == 0:
            new_list.append(i)
    print(new_list)


def upper_string():
    original_list = ['rohan', 'eshan', 'mama', 'papa']
    new_list = []
    for i in range(4):
        new_word = original_list[i]
        new_list.append(new_word.upper())
    print(new_list)


even_sorter()
upper_string()


