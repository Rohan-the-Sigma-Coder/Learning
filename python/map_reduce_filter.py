import math
from functools import reduce
def is_prime_filter(num):
    if num < 2:
        return False
    factor_list = []
    square_root = math.ceil(num ** 0.5)
    for test_num in range(1, square_root + 1):
        if num % test_num == 0:
            factor_list.append(test_num)
    if len(factor_list) == 1:
        return True
    else:
        return False


words = ["machine", "learning", "is", "super", "fun", "and", "powerful"]
a = filter(lambda x: len(x) > 3, words)
b = map(lambda y: y.upper(), list(a))
c = reduce(lambda x, y: x + ' ' + y, list(b))
print(c)

