# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(nums1)
print(nums2)

def mergeSortedArray(nums1, m, nums2, n):
    # Initialize nums1's index
    i = m - 1
    # Initialize nums2's index
    j = n - 1
    # Initialize a variable k to store the last index of the 1st array...
    k = m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1


mergeSortedArray(nums1, m, nums2, n)

print(nums1)