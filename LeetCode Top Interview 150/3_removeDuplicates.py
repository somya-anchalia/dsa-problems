from typing import List

def removeDuplicates(nums: List[int]) -> int:
    length = len(nums)
    unique_dict = {}
    for i in range(length):
        if nums[i] in unique_dict.keys():
            unique_dict[nums[i]] += 1
        else:
            unique_dict[nums[i]] = 1
    unique_list = list(unique_dict.keys())
    print(nums)
    for i in range(len(unique_list)):
        nums[i] = unique_list[i]
    print(nums)
    return len(unique_list)


nums = [0,0,1,1,1,2,2,3,3,4]
length = removeDuplicates(nums)
print(length)