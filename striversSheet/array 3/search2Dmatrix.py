matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 5

def search(matrix, target):

    for i in matrix:
        l = 0
        r = len(i)-1
        while l<=r:
            mid = l+(r-l) // 2
            if target == i[mid]:
                return True
            elif target < i[mid]:
                r = mid-1
            else:
                l = mid+1
    return False


print(search(matrix, target))
