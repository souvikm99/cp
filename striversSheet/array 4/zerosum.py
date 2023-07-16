#sol: https://youtu.be/Bne92MpRieE

n = 6
arr = [9, -3, 3, -1, 6, -5]
dict = {0:-1}
longest = 0
# print(dict[0])
sum = 0
for i in range(len(arr)):
    sum += arr[i]
    if sum not in dict:
        dict[sum] = i
    else:
        # cur_subarr = arr[dict[sum]-i:i+1]
        # print(cur_subarr)
        cur_len = i - dict[sum]

        if cur_len > longest:
            longest = cur_len
        else:
            cur_len = 0

print(dict)
print(longest)
