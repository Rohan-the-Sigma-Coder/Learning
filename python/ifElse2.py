s = input('Enter your state: ')
p = int(input("Enter the price of item in dollars (Don't add the dollar sign, just the whole number): "))
if s=='Florida' or p>10:
    print('Sales tax is applicable')
else:
    print('Only local taxes applicable')
