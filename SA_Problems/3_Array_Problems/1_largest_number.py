
def findLargestElement(arr, n):
    max = arr[0]
    for i in range(0, n):
        if (max < arr[i]):
            max = arr[i]
    return max

arr1 = [2, 5, 1, 3, 0]
n = 5
max = findLargestElement(arr1, n)
print("The largest element in the array is:", max)

arr2 = [8, 10, 5, 7, 9]
n = 5
max = findLargestElement(arr2, n)
print("The largest element in the array is:", max)

# Second method - BRUTE FORCE

from typing import List

def sortArr(arr: List[int]) -> int:
    arr.sort()
    return arr[-1]

arr1 = [2, 5, 1, 3, 0]
arr2 = [8, 10, 5, 7, 9]
print("The Largest element in the array is:", sortArr(arr1))
print("The Largest element in the array is:", sortArr(arr2))