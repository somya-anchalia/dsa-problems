def isPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        # skip left if not alphanumeric
        if not s[left].isalnum( ):
            left += 1
        # skip right if not alphanumeric
        elif not s[right].isalnum():
            right -= 1
        # convert to lowercase and compare
        elif s[left]. lower() != s[right].lower():
            return False
        # move both pointers
        else:
            left += 1
            right -= 1
    return True

text = "A man, a plan, a canal: Panama"

print(f"Given text is Palindrome : {isPalindrome(text)}")