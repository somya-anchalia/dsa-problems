# **** Array Challenge ****

# Have the function ArrayChallenge (strArr) read the array of strings stored in strArr, which will contain 2 elements: 
# the first element will be a sequence of characters, and the second element will be a long string of comma-separated words, 
# in alphabetical order, that represents a dictionary of some arbitrary length.
# For example: strArr can be: ['hellocat", "apple, bat,cat,goodbye,hello,yellow,why"].
# Your goal is to determine if the first element in the input can be split into two words, where both words exist in the 
# dictionary that is provided in the second input. In this example, the first element can be split into 
# two words: hello and cat because both of those words are in the dictionary.
# Your program should return the two words that exist in the dictionary separated by a comma. 
# So for the example above, your program should return hello, cat. 
# There will only be one correct way to split the first element of characters into two words.
# If there is no way to split string into two words that exist in the dictionary, return the string not possible. 
# The first element itself will never exist in the dictionary as a real word.

# Once your function is working, take the final output string and concatenate it with your ChallengeToken, 
# and then replace every third character with an X.
# Your ChallengeToken: ucwvesj137b


def ArrayChallenge(strArr):
    word = strArr[0]
    dictionary = strArr[1].split(',')

    # Try to split the word into two parts
    for i in range(1, len(word)):
        part1 = word[:i]
        part2 = word[i:]
        if part1 in dictionary and part2 in dictionary:
            result = f"{part1},{part2}"
            break
    else:
        result = "not possible"

    # Your ChallengeToken
    ChallengeToken = "ucwvesj137b"

    # Concatenate the result with the ChallengeToken
    final_output = result + ChallengeToken

    # Replace every third character with 'X'
    final_output = ''.join(
        'X' if (i + 1) % 3 == 0 else char
        for i, char in enumerate(final_output)
    )

    return final_output

# Example usage:
strArr = ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]
print(ArrayChallenge(strArr))
