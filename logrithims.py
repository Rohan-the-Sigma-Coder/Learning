import math

perfect_log = True
answer = 0

argument = int(input("Enter argument: "))
base = int(input("Enter base: "))

def logrithim_calculator(perfect_log, answer, argument, base):
    while argument > 1:
        if argument % base == 0:
            argument = argument/base
        else:
            perfect_log = False
            break
        answer += 1


    if perfect_log == True: 
        return answer
    else:
        return "Not a perfect logrithim"
    


print(logrithim_calculator(perfect_log, answer, argument, base))