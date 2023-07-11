def mergeLike(arr):
    count = 0

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        count += mergeLike(left)
        count += mergeLike(right)

        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] > 2 * right[j]:
                count += len(left) - i  # Increment count by the remaining elements in the left array
                j += 1
            else:
                i += 1

        arr[:] = sorted(arr)  # Merge the sorted left and right arrays back into the original array

    return count


nums = [-5,-5]
print(mergeLike(nums))
