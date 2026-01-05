import math
import time

def is_prime(num):
    is_prime = True
    start_time_ms = time.perf_counter_ns() / 1_000_000    
    squared_num = math.sqrt(num)
    squared_num = math.ceil(squared_num)
    squared_num = num
    for i in range(2, squared_num + 1):
        if num % i == 0:
            is_prime = False
            break
    end_time_ms = time.perf_counter_ns() / 1_000_000    
    runtime_ms = end_time_ms - start_time_ms
    return is_prime, runtime_ms

    

num = int(input("Enter number: "))
result, runtime_ms = is_prime(num)
print(result)
print(f"It took {runtime_ms} milliseconds to run the program")
