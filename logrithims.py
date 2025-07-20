import math

argument = int(input("Enter argument: "))
base = int(input("Enter base: "))
bool = True
answer = 0

while argument > 1:
    if argument % base == 0:
        argument = argument/base
    else:
        bool = False
        print('It is not perfect logrithim')
        break
    answer += 1


if bool == True: print(answer) 