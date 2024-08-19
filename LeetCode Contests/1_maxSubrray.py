# Find the Power of K-Size Subarrays I

# You are given an array of integers nums of length n and a positive integer k.
# The power of an array is defined as:
# Its maximum element if all of its elements are consecutive and sorted in ascending order.
# -1 otherwise.
# You need to find the power of all 
# subarrays
#  of nums of size k.

# Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

# Example 1:
# Input: nums = [1,2,3,4,3,2,5], k = 3
# Output: [3,4,-1,-1,-1]
# Explanation:
# There are 5 subarrays of nums of size 3:

# [1,4]

from typing import List

def resultsArray(nums: List[int], k: int) -> List[int]:
    len_sub_array = len(nums) - k + 1
    sub_arrays = []

    if k == 1:
        return nums
    elif len(nums) == k:
        sub_arrays.append(max(nums))
        return sub_arrays

    if len(nums) > k:
        for i in range(len_sub_array):
            sub_array = nums[i:k+i]
            pattern = True
            if k > 1:
                pattern = False
                for j in range(k-1):
                    if sub_array[j+1] == sub_array[j]+1:
                        pattern = True
                    else:
                        pattern = False
                        break
            if pattern:
                sub_arrays.append(max(sub_array))
            else:
                sub_arrays.append(-1)
        return sub_arrays
