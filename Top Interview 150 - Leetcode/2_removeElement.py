# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

from typing import List
nums = [3,2,2,3]
val = 3

def removeElement(nums: List[int], val: int) -> int:
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index

index = removeElement(nums, val)
print(index)