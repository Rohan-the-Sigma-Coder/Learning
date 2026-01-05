import math

def binary_to_decimal(binary):
    result = 0
    binary = list(map(int, str(binary)))
    binary.reverse()
    for i in range(len(binary)):
        if binary[i] == 1:
            result += 2 ** i
    return result

def decimal_to_binary(decimal):
    binary_list = []
    while decimal > 0:
        remainder = decimal % 2
        decimal = math.floor(decimal / 2)
        if remainder == 1:
            binary_list.append(1)
        else:
            binary_list.append(0)
    return binary_list[::-1]



def binary_calculator(binary1, operation, binary2):
    decimal1 = binary_to_decimal(binary1)
    decimal2 = binary_to_decimal(binary2)
    if operation == "+":
        decimal = decimal1 + decimal2
    if operation == "-":
        decimal = decimal1 - decimal2
    if operation == "*":
        decimal = decimal1 * decimal2
    if operation == "/":
        decimal = decimal1 // decimal2
    
    binary_result = decimal_to_binary(decimal)
    return binary_result, decimal


binary1 = int(input("Enter first binary number: ").strip())
operation = input("Enter operation: ")
binary2 = int(input("Enter second binary number: ").strip())

binary_result, decimal_result = binary_calculator(binary1, operation, binary2)
print(*binary_result)
print(decimal_result)

        
