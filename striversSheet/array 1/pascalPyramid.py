# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:

# Input: numRows = 1
# Output: [[1]]

#--------------------%--------------------#




def pascal(numRows):
    prev = [[1],[1,1]]
    if numRows == 1:
        return [prev[0]]
    elif numRows == 2:
        return prev
    else:
        for i in range(2, numRows):
            cur = []
            for i in range(len(prev[-1])+1):
                cur.append(1)
            for i in range(1, len(cur)-1):
                cur[i] = prev[-1][i-1]+prev[-1][i]

            prev.append(cur)
        return prev


res = pascal(1)
print(res)
    
