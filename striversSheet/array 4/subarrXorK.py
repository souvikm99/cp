#sol : https://www.youtube.com/watch?v=lg7cLOP5uLk

A = [4, 2, 2, 6, 4] 
k = 6


def xorSum(A,k):
    dict = {0:1}
    count = 0
    xr = 0
    for i in range(len(A)):
        xr ^= A[i]
        y = xr^k
        if y in dict:
            count += dict[y]

        if xr in dict:
            dict[xr] += 1
        else:
            dict[xr] = 1

    return count

print(xorSum(A,k))