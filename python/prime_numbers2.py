import math
import time

def prime_numbers(num):
    start_time = time.perf_counter_ns() / 1_000_000    
    factors = []
    squared_num = math.sqrt(num)
    squared_num = math.ceil(squared_num)
    for i in range(1, squared_num + 1):
        if num % i == 0:
            factors.append(i)
    factors.sort()
    end_time = time.perf_counter_ns() / 1_000_000    
    difference = end_time - start_time
    if len(factors) == 1:
        return "Prime Number", difference
    else:
        return num, difference

num = int(input("Enter number: "))
result, difference = prime_numbers(num)
print(result)
print(f"It took {difference} milliseconds to run the program")
