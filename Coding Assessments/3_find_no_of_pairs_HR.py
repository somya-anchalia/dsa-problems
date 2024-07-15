# Consider two arrays of integers, a[n] and b[n]. What is the maximum number of pairs that can be formed where a[i] > b[j]? Each element can be in no more than one pair.
# Find the maximum number of such possible pairs.
# Example n =3
# a = 11, 2,31
# b= 11,2,11
# Two ways the maximum number of pairs can be selected:
# • (a[1], b[0])-{2, 1} and {a[2], b[2]}-{3,1} are valid pairs.
# • {a[1], b[0]}-(2, 1) and {a[2], b[1]=(3, 2) are valid pairs.
# No more than 2 pairs can be formed, so return 2.
# Function Description:
# findNumOfPairs has the following parameters: int a[n]: an array of integers int b[n]: an array of integers
# Returns
# int: the maximum number of pairs

def findNumOfPairs(a, b):
    # Sort both arrays
    a.sort()
    b.sort()

    # Initialize pointers and counter for pairs
    i = 0
    j = 0
    pairs = 0

    # Iterate through both arrays
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            # Form a pair
            pairs += 1
            j += 1
        # Move to the next element in a
        i += 1

    return pairs

# Example usage
a = [11, 2, 31]
b = [11, 2, 11]
result = findNumOfPairs(a, b)
print(result)  # Output: 2
