from typing import List

def singleNumber(nums: List[int]) -> int:
    duplicates = {}
    for i in range(len(nums)):
        if nums[i] in duplicates.keys():
            duplicates[nums[i]] = True
        else:
            duplicates[nums[i]] = False
    for key, value in duplicates.items():
        if not value:
            return key

nums = [4,1,2,1,2]
answer = singleNumber(nums)
print(answer)