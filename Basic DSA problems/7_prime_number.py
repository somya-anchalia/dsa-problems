                                
# Function to check if a
# given number is prime.
def checkPrime(n):
    # Initialize a counter variable to
    # count the number of factors.
    cnt = 0
    # Loop through numbers from 1 to n.
    for i in range(1, n+1):
        # If n is divisible by i
        # without any remainder.
        if n % i == 0:
            # Increment the counter.
            cnt = cnt + 1

    # If the number of
    # factors is exactly 2
    if cnt == 2:
        # Return True, indicating
        # that the number is prime.
        return True
    # If the number of
    # factors is not 2.
    else:
        # Return False, indicating
        # that the number is not prime.
        return False

if __name__ == "__main__":
    n = input("Provide a number to check if it's prime : ")
    isPrime = checkPrime(int(n))
    if isPrime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")
                                
                            