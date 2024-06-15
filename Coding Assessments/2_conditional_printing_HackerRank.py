# **** Conditional Printing Challenge ****

# FizzBuzz
# Given a number n, for each integer i in the range from 1 to n inclusive, print one value per line as follows:
# *If iis a multiple of both 3 and 5, print FizzBuzz.
# • If /is a multiple of 3 (but not 5), print Fizz.
# • If /is a multiple of 5 (but not 3), print Buzz.
# • If /is not a multiple of 3 or 5, print the value of i.

#!/bin/python3

import math
import os
import random
import re
import sys

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)
