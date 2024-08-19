# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

def removeDuplicates_II(nums):
    # Initialize an integer k that updates the kth index of the array
    # only when the current element does not match either of the two previous indexes
    k = 0

    # Traverse all elements through loop...
    for i in nums:
        # If the index does not match elements, count that element and update it
        if k < 2 or i != nums[k - 2]:
            nums[k] = i
            k += 1

    return k       # Return k after placing the final result in the first k slots of nums

nums = [0,0,1,1,1,2,2,3,3,4]
length = removeDuplicates_II(nums)
print(length)
