import math
import time

def is_prime(num):
    factor_list = []
    prime_num_list = []
    square_root = num ** 0.5
    if num % square_root != 0:
        square_root = math.ceil(square_root)
    square_root = int(square_root)
    for i in range(1, square_root + 1):
        if num % i == 0:
            factor_list.append(i)
    if len(factor_list) == 1:
        # return "PRIME NUMBER"
        return True
    else:
        return False


def prime_num_generator():
    startTimeInSec = time.time()
    for number in range(100000, 200000):
        if is_prime(number):
            print(f'{number} --> PRIME NUMBER ')
        else:
            print(number)
    endTimeInSec = time.time()
    print(f'Time it took for program to run: approximately {round(endTimeInSec - startTimeInSec, 3)} seconds')


print(is_prime(3))




