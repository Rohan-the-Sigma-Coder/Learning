for i in range(4):
    n = int(input('Enter the height of student to nearest whole feet[Press 0 to end]: '))
    max = n
    while (n != 0):
        n = int(input('Enter the height of student to nearest whole feet [Press 0 to end]: '))
        if(n>max):
            max = n 
        print('Tallest student is ' + str(max))