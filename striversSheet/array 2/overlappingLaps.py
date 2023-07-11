# Merge Overlapping Sub-intervals

# Problem Statement: Given an array of intervals, 
# merge all the overlapping intervals and return an array of non-overlapping intervals.

# Examples

# Example 1:

# Example 1: 

# Input: intervals=[[1,3],[2,6],[8,10],[15,18]]

# Output: [[1,6],[8,10],[15,18]]

# Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
#  intervals.

# Example 2:

# Input: [[1,4],[4,5]]

# Output: [[1,5]]

# Explanation: Since intervals [1,4] and [4,5] are overlapping we can merge them to form [1,5].




intervals=[[0,1],[0,0]]
intervals.sort()
print(intervals)

# Output: [[1,6],[8,10],[15,18]]

def check(arr):
    lis = [intervals[0]]
    for i in intervals:
        if max(i)-min(i) <= 0:
            lis.append(i)
        elif min(i) <= max(lis[-1]) and max(i) <=max(lis[-1]) and min(i) >= min(lis[-1]):
            continue
        elif min(i) <= max(lis[-1]) and min(i)>min(lis[-1]):
            lis[-1][-1] = max(i)
        elif min(i)<=min(lis[-1]):
            lis[-1][0] = min(i)
            lis[-1][-1] = max(max(lis[-1]),max(i))
        else:
            lis.append(i)
    return lis



print(check(intervals))