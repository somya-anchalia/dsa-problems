                            
# Function to check if a
# given integer is a palindrome
def palindrome(n):
    # Initialize a variable to
    # store the reverse of the number
    revNum = 0
    # Create a duplicate variable to
    # store the original number
    dup = n
    # Iterate through each digit of
    # the number until it becomes 0
    while n > 0:
        # Extract the last
        # digit of the number
        ld = n % 10
        # Build the reverse number
        # by appending the last digit
        revNum = (revNum * 10) + ld
        # Remove the last digit
        # from the original number
        n = n // 10
    # Check if the original number
    # is equal to its reverse
    if dup == revNum:
        # If equal, return True
        # indicating it's a palindrome
        return True
    else:
        # If not equal, return False
        # indicating it's not a palindrome
        return False


def main():
    number = 4554

    if palindrome(number):
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")


if __name__ == "__main__":
    main()
                           
                        