def binary_converter(d):
    binary_list = []
    while d > 0:
        r = d % 2
        q = d//2
        binary_list.append(r)
        d=q
    binary_list = binary_list[::-1]
    return binary_list



# d = int(input('Enter a number: '))
expected_list = [1, 0, 0]
result_list = binary_converter(4)
if result_list == expected_list:
    print('Program test pass')
else:
    print("PROGRAM TEST FAIL")



