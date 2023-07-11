arr = [52244275, 
       123047899, 493394237, 
       922363607, 378906890, 
       188674257, 222477309, 
       902683641, 860884025, 
       339100162]

# count = 0
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#             if arr[i] > arr[j]:
#                 count+=1

# print(count)

def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = mergeSort(arr[:mid])
    right, inv_right = mergeSort(arr[mid:])

    merged, inversions = merge(left, right)

    return merged, inv_left + inv_right + inversions


def merge(left, right):
    merged = []
    inversions = 0
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions


# Example usage
inversions = mergeSort(arr)[1]
print("Number of inversions:", inversions)
