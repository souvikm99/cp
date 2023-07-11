# 287. Find the Duplicate Number


# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3


nums = [1,3,4,3,2]

# temp = 0
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         if i != j:
#             if nums[i] == nums[j]:
#  
# 
#                temp = nums[i]
# temp = 0
# while temp < len(nums):
#     for i in range(temp, len(nums)):
#         if temp != i:
#             if nums[temp]-nums[i] == 0:
#                 print(nums[i])
#                 temp = len(nums)
#                 break
#     temp += 1

nums.sort()
for i in range(len(nums)):
    if i < len(nums)-1:
        if nums[i]-nums[i+1] == 0:
            print(nums[i])
#faster ->
b = set()
for i in nums:
    if i not in b:
        b.add(i)
    else:
        print("FASTER RESULT -> ",i)
        
        


