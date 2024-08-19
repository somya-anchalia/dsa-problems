from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n  # In case k is larger than n
    
    # Helper function to reverse a portion of the array
    def reverse_array(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    # Reverse the entire array
    reverse_array(0, n - 1)
    # Reverse the first k elements
    reverse_array(0, k - 1)
    # Reverse the remaining n - k elements
    reverse_array(k, n - 1)

nums = [1,2,3,4,5,6,7]
k = 3
print(nums)
length = rotate(nums,k)
print(nums)
