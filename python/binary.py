def decimal_to_binary(d):
    binary_list = []
    while d > 0:
        r = d % 2
        d = d//2
        binary_list.append(r)
    binary_list = binary_list[::-1]
    return binary_list



# d = int(input('Enter a number: '))
# expected_list = [1, 0, 0]
# result_list = decimal_to_binary(4)
# if result_list == expected_list:
#     print('Program test pass')
# else:
#     print("PROGRAM TEST FAIL")




def binary_to_decimal(binary):
     result_list = []
     binary_list = list(map(int, str(binary)))
     for i in range(len(binary_list)):
         if binary_list[i] == 1:
             result_list.append(2**i)
     return sum(result_list)


binary = input('Binary number: ')

try:
    binary = int(binary)
except:
    print('Invalid Input')
print(binary_to_decimal(binary))
         




