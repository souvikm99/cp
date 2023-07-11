nums = [3,2,3]
nums.sort()
# print(nums)
count = 1
for i in range(len(nums)):
    
    if i < len(nums)-1:
        if nums[i+1] - nums[i] == 0:
            count += 1
            # print(count)
        else:
            count = 1
    if count > len(nums)/2:
        print(nums[i])
        break
    
