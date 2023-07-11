#revisit = https://www.youtube.com/watch?v=P1Ic85RarKY

nums1 = [4]
m = 1
nums2 = []
n = 0

last = m+n-1

while m > 0  and n > 0:
    if nums1[m-1] > nums2[n-1]:
        nums1[last] = nums1[m-1]
        m -= 1
    else:
        nums1[last] = nums2[n-1]
        n -= 1
    last -= 1

while n>0:
    nums1[last] = nums2[n-1]
    n -= 1
    last -= 1

# i = 1
# arr = nums1[i:i+3]

# print(arr)

# for i in range(m):
#     if n > 0:
#         min_all = min(min(nums1[i:m]),min(nums2))
#         if min_all in nums1[i:n]:
#             continue
#         else:
#             for j in range(n):
#                 if nums2[j] == min_all:
#                     nums1[i],nums2[j] = nums2[j], nums1[i]
#         nums2.sort()

#         for i in range(n):
#             nums1[m+i] = nums2[i]
#     else:
#         nums1.sort()


print(nums1)
print(nums2)