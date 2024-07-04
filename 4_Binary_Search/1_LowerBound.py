
def brute_force_lowerBound(arr: [int], n: int, x: int) -> int:
    for i in range(n):
        if arr[i] >= x:
            #lower bound found
            return i
    return n

def optimal_lowerBound(arr: [int], n: int, x: int) -> int:
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ind = optimal_lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)

