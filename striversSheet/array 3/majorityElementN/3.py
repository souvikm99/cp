# Majority Elements(>N/3 times) | Find the elements that appears more than N/3 times in the array

# Problem Statement: Given an array of N integers. Find the elements that appear more than N/3 times 
# in the array. If no such element exists, return an empty vector.

# Pre-requisite: Majority Element(>N/2 times)

# Examples

# Example 1:
# Input Format: N = 5, array[] = {1,2,2,3,2}
# Result: 2
# Explanation: Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, 
# the count of 2 is greater than N/3 times. Hence, 2 is the answer.

# Example 2:
# Input Format:  N = 6, array[] = {11,33,33,11,33,11}
# Result: 11 33
# Explanation: Here we can see that the Count(11) = 3 and Count(33) = 3. Therefore, 
# the count of both 11 and 33 is greater than N/3 times. Hence, 11 and 33 is the answer.

######################################################################################################

nums = [1,2,3]
nums.sort()
# print(nums)
count = 1
temp = []
for i in range(len(nums)):

    if i < len(nums)-1:
        if nums[i+1] - nums[i] == 0:
            count += 1
            # print(count)
        else:
            count = 1        
    if count > len(nums)/3:
        temp.append(nums[i])

print(list(set(temp)))

        
