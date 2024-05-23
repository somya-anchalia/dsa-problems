#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

def diamond_pattern(n):
    # Upper half of the diamond
    for i in range(n):
        for j in range(n - 1, i, -1):
            print(" ", end="")
        for k in range(i + 1):
            print("* ", end="")
        print()

    # Lower half of the diamond
    for i in range(1, n):
        for j in range(i):
            print(" ", end="")
        for k in range(n - 1, i - 1, -1):
            print("* ", end="")
        print()

def butterfly_pattern(n):
    # Upper half of the butterfly
    for i in range(1, n + 1):
        # Print left stars
        for j in range(i):
            print("*", end="")
        # Print spaces
        for j in range(2 * (n - i)):
            print(" ", end="")
        # Print right stars
        for j in range(i):
            print("*", end="")
        print()

    # Lower half of the butterfly
    for i in range(n, 0, -1):
        # Print left stars
        for j in range(i):
            print("*", end="")
        # Print spaces
        for j in range(2 * (n - i)):
            print(" ", end="")
        # Print right stars
        for j in range(i):
            print("*", end="")
        print()

diamond_pattern(5)
butterfly_pattern(6)