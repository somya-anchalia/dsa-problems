
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
    for i in range(len(unique_list)):
        nums[i] = unique_list[i]
    return len(unique_list)


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = removeDuplicates(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")
    print()

