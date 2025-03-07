num = 1
list = [1, 2, 3, 4, 5]
for i in range(5):
    list.remove(int(num))
    list.insert(num-1, num*2)
    num += 1
print(list)