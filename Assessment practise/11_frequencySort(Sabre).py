# https://leetcode.com/problems/sort-array-by-increasing-frequency/solutions/

def frequencySort(nums):
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    print(d)
    nums.sort(reverse=True)
    print(nums)
    nums.sort(key=lambda x:d[x])
    print(nums)
    return nums


list = [-1,1,-6,4,5,-6,1,4,1]
print(list)
sorted_list = frequencySort(list)
print(sorted_list)