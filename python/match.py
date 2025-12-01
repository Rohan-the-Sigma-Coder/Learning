def calculator(a, b, operation):
    match operation:
        case 'add':
            return a + b
        case 'subtract':
            return a - b
        case 'multiply':
            return a * b
        case 'divide':
            return a / b
        case _:
            return 'Invalid Operation'
        

print(calculator(10, 5, "add"))       
print(calculator(10, 5, "subtract"))  
print(calculator(10, 5, "multiply"))  
print(calculator(10, 5, "divide"))   
print(calculator(10, 5, "mod"))       