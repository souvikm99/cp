nums = [-2,1,-3,4,-1,2,1,-5,4]
import sys
max_size = sys.maxsize
min_size = -sys.maxsize - 1

def maxSubSum(nums):
    import sys
    max_size = sys.maxsize
    min_size = -sys.maxsize - 1
    # if len(nums) == 1:
    #     return nums[0]
    # else:
    #     ult_sum = min_size
    #     for i in range(len(nums)):
    #         sum = None
    #         max_sum = min_size
    #         for j in range(i, len(nums)):
    #             if sum == None:
    #                 sum = nums[j]
    #             else:
    #                 sum = sum + nums[j]
    #             if sum > max_sum:
    #                 max_sum = sum
    #         if ult_sum < max_sum:
    #             ult_sum = max_sum
    #     return ult_sum
    sum = 0
    max_sum = min_size
    for i in range(len(nums)):
        sum = sum + nums[i]
        if sum > max_sum:
            max_sum = sum
        if sum < 0:
            sum = 0
    return max_sum

print(maxSubSum(nums))

