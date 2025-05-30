nums = [1, 2, 4, 8, 16]

for i in range(1, len(nums), -1):
    nums.append(nums[i] / i)


print(nums)
