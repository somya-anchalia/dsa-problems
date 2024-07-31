# https://takeuforward.org/data-structure/find-the-repeating-and-missing-numbers/

from typing import List

def findMissingRepeatingNumbers(a: [int]) -> [int]:
    n = len(a) # size of the array
    hash = [0] * (n + 1) # hash array

    #update the hash array:
    for i in range(n):
        hash[a[i]] += 1

    #Find the repeating and missing number:
    repeating, missing = -1, -1
    for i in range(1, n + 1):
        if hash[i] == 2:
            repeating = i
        elif hash[i] == 0:
            missing = i

        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]

if __name__ == '__main__':
    a = [3, 1, 2, 5, 6, 7, 3]
    ans = findMissingRepeatingNumbers(a)
    print("The repeating and missing numbers are: {", ans[0], ", ", ans[1], "}\n")
