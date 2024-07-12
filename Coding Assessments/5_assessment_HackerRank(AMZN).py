# AWS provides scalable systems. A set of n servers are used for horizontally scaling an
# application. The goal is to have the computational power of the servers in increasing order.
# To do so, you can increase the computational power of each server in any contiguous segment by x. Choose the values of x such that after the computational powers are in non-decreasing order, the sum of the x values is minimum.
# Example 1:
# There are n = 5 servers and their computational power = [3, 4, 1, 6, 2].
# Add 3 to subarray (1,6,2) so array becomes [3, 4, 4, 9, 5] and then add 4 to subarray (5) so array final increasing order array becomes [3, 4, 4, 9, 9]. The answer is 3 + 4 = 7.

# Example 2: 
# There are n = 5 servers and their computational power = [3, 3, 2, 1]. Add 1 to subarray (2,1) so array becomes [3,3,3,2] and then add 1 to subarray (2) so array final increasing order array becomes [3,3,3,3]. The answer is 1+1=2

# Function Description
# Complete the function makePowerNonDecreasing that has the following parameter:
# int power[n]: the computational powers of n different servers
# Returns
# int: the minimum possible sum of integers required to make the array increasing order

def makePowerNonDecreasing(power):
    n = len(power)
    total_increase = 0

    for i in range(1, n):
        if power[i] < power[i - 1]:
            increment = power[i - 1] - power[i]
            total_increase += increment
            for j in range(i,n):
                power[j] += increment

    return total_increase

# Example usage
power1 = [3, 4, 1, 6, 2]
print(makePowerNonDecreasing(power1))  # Output: 7

power2 = [3, 3, 2, 1]
print(makePowerNonDecreasing(power2))  # Output: 2
