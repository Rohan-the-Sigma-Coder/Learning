a = input('Enter first number: ')
b = input('Enter second number: ')
c = input('Enter third number: ')
if a>b and b>c:
    print('Numbers in descending order: ', a, b, c)
elif a<b and b<c:
    print('Numbers in descending order: ', c, b, a)
elif a>b and c>a:
    print('Numbers in descending order: ', c, a, b)
elif a<b and b>c and c>a:
    print('Numbers in descending order: ', b, c, a)
elif a>c and c>b:
    print('Numbers in descending order: ', a, c, b)
elif b>a and a>c:
    print('Numbers in descending order: ', b, a, c)