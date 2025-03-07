x = int(input('Enter a number I will show you the factorial for that number: '))
factorial = 1
for i in range(x,0,-1):
    factorial *= i
print(factorial)