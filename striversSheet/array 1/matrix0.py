# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

#--------------------%--------------------#

matrix = [[-1],[2],[3]]
print(matrix)
Zindex = set()
for i in range(len(matrix)):

    for j in range(len(matrix[i])):
        # print(matrix[i][j])
        if int(matrix[i][j])==0:
            Zindex.add(j)
            for k in range(len(matrix[i])):
                if matrix[i][k] != 0:
                    matrix[i][k]='k'

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]!='k':
            if j in Zindex:
                matrix[i][j]='k'

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]=='k':
            matrix[i][j]=0

print(matrix)