# Better Compression: 

# Consider a string, 5, that is a series of characters, each followed by its frequency as an integer. The string is not compressed correctly, so there may be multiple occurrences of the same character. A properly compressed string will consist of one instance of each character in alphabetical order followed by the total count of that character within the string

# Example: The string 'a3c9b2c1’ has two instances where ‘c’ is followed by a count: once with 9 occurrences, and again with 1. It should be compressed to 'a3b2c10:

# Function Description
# Complete the function betterCompression

# betterCompression function has the following parameter:

# S: a compressed string

# Function Returns:
# string: the properly compressed string


def betterCompression(S):
    from collections import defaultdict
    
    # Dictionary to store total counts of each character
    char_count = defaultdict(int)
    
    # Temporary variables to store current character and frequency
    i = 0
    while i < len(S):
        char = S[i]
        i += 1
        num = 0
        while i < len(S) and S[i].isdigit():
            num = num * 10 + int(S[i])
            i += 1
        char_count[char] += num
    
    # Create the resulting string in alphabetical order
    result = []
    for char in sorted(char_count.keys()):
        result.append(char + str(char_count[char]))
    
    return ''.join(result)

# Example Usage
S = 'a3c9b2c1'
print(betterCompression(S))  # Output: 'a3b2c10'
