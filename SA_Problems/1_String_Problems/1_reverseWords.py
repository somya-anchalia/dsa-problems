def reverseWords(s: str) -> str:

    # Split the string into words
    words = s.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed words with spaces
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

print("hello world")
print(reverseWords("hello world"))