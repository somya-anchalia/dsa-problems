import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1 # maximum sum

    for i in range(n):
        sum = 0
        for j in range(i, n):
            # current subarray = arr[i.....j]

            #add the current element arr[j]
            # to the sum i.e. sum of arr[i...j-1]
            sum += arr[j]

            maxi = max(maxi, sum) # getting the maximum

    return maxi

arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)

