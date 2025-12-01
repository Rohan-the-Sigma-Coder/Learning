vowels = 0
spaces = 0
consonants = 0
list_num = 0
vowels_list = ['a', 'e', 'i', 'o', 'u']
try:
    user_input = input('Enter string: ').lower()
except ValueError:
    print('Invalid input')
    quit()
input_list = list(user_input)
for i in range(len(input_list)):
    if input_list[i-1] == ' ':
        spaces += 1
    elif input_list[i - 1] in vowels_list:
        vowels += 1
       
    else:
        consonants += 1
    list_num += 1
output = 'There was {} vowels, {} consonants, and {} spaces in the string'
print(output.format(vowels, consonants, spaces))


