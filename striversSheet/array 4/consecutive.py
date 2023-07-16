nums = [100,4,200,1,3,2]
def maxConsecutive(nums):
    nums.sort()
    print(nums)
    if len(nums) == 0:
        return 0
    elif len(nums) == 1 or len(set(nums))==1:
        return 1
    else:
        count = 0
        count_all = [0]
        nums = list(set(nums))
        nums.sort()
        print(nums)

        for i in range(len(nums)-1):
            if abs(nums[i]-nums[i+1]) == 1:
                # print(i)
                count += 1
                count_all.append(count)
            else:
                
                # print(count_all, nums[i])
                count = 0
                continue
        return max(count_all)+1
    
print("res : ", maxConsecutive(nums))

        

