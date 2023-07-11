nums = [2,0,1]

import sys
max_size = sys.maxsize
for i in range(len(nums)):
    min = max_size
    min_idx = None

    for j in range(i,len(nums)):
        if nums[j] < min:
            min = nums[j]
            min_idx = j
    if min_idx != None:
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

print(nums)
