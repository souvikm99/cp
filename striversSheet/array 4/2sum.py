nums = [3,3]
target = 6

dict = {}

for i, num in enumerate(nums):
    if num in dict:
        print ([i]+[dict[num]])
    else:
        dict[target - num] = i

