def star_pyramid():
    spaces = 5
    for i in range(1, 10, 2):
        print(' ' * spaces + '*' * i)
        spaces -= 1
    spaces = 1
    for x in range(9, 1, -2):
        print(' ' * spaces + '*' * x)
        spaces += 1



star_pyramid()