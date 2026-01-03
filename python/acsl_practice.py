n = int(input("Enter number: "))
p = int(input("Enter Pth digit: "))

n = list(map(int, str(n)))

reversed_n = n[::-1]
p_value = reversed_n[p-1]
print(p_value)
p = n.index(p_value)
left_side = n[:p]
right_side = n[p+1:]
print(left_side)
print(right_side)
print(p)
print(reversed_n)

for digit in range(len(left_side)):
    number = left_side[digit] + p_value
    if number > 9:
        number %= 10
        left_side[digit] = number
    else:
        left_side[digit] = number

left_side.append(p_value)

for digit in range(len(right_side)):
    right_side[digit] = abs(p_value - right_side[digit])

result = left_side + right_side
print(result)
string_list = [str(i) for i in result]
joined_string = "".join(string_list)
result = int(joined_string)
print(result)