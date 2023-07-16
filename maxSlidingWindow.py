#sol : https://www.youtube.com/watch?v=MCvGwtkqJS0

nums = [1]
k = 1

# print(nums[0:1])
from collections import deque

def findMax(nums, k):

    res = []
    deq = deque()

    for i in range(len(nums)):
        if deq and deq[0]<=i-k:
            deq.popleft()
        
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        if i>=k-1:
            res.append(nums[deq[0]])

    return res

print(findMax(nums,k))

'''In the line while window and nums[window[-1]] < nums[i]:, the code checks two conditions in the while loop:

    window: This condition checks if the window deque is not empty. It ensures that there are elements present in the deque that need to be compared and potentially popped.

    nums[window[-1]] < nums[i]: This condition checks if the value of the element at the back of the deque (denoted by window[-1]) is less than the value of the current element nums[i].

Let's break down what this line does:

    window[-1] refers to the last index stored in the deque, representing the index of an element that was previously seen in the window.
    nums[window[-1]] retrieves the value of the element at index window[-1] from the nums array.
    nums[i] represents the value of the current element being processed.

So, the condition nums[window[-1]] < nums[i] compares the values of the last element in the deque with the current element. If the value of the current element is greater, it means the current element is a potential candidate to be the maximum in the window.

If the condition evaluates to True, the while loop continues, indicating that the element at the back of the deque is smaller than the current element. In this case, we remove that element from the deque using window.pop(). We repeat this process until the condition becomes False, meaning we have either removed all smaller elements from the back of the deque or the deque is empty.

This ensures that the deque remains sorted in descending order of element values, with the maximum element at the front of the deque. By comparing and removing elements from the back of the deque as necessary, we maintain the property of having the maximum element at the front as we iterate through the array.



The code block `if i >= k - 1: result.append(nums[window[0]])` is responsible for appending the maximum element for the current window to the `result` list. 

Let's break it down:

- `i` represents the current index of the array `nums` that we are iterating over.
- `k` is the window size, representing the number of elements we can see in each window.

The condition `i >= k - 1` is used to check if we have processed enough elements to form a complete window. When `i` becomes greater than or equal to `k - 1`, it means we have processed at least `k` elements, and we can start adding the maximum element for each subsequent window.

Inside the condition, `result.append(nums[window[0]])` adds the maximum element for the current window to the `result` list. 

- `window[0]` represents the index stored at the front of the deque, which corresponds to the index of the maximum element in the current window.
- `nums[window[0]]` retrieves the value of the maximum element from the `nums` array using the index stored in `window[0]`.
- `result.append(nums[window[0]])` adds this maximum element to the `result` list.

By adding the maximum element to the `result` list only when we have processed enough elements to form a complete window, we ensure that the `result` list contains the maximum elements for each sliding window of size `k`.

Once all the windows have been processed, the `result` list will contain the maximum elements for each window in the original input array.

'''