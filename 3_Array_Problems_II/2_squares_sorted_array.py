# https://leetcode.com/problems/squares-of-a-sorted-array/description/

from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    return sorted(list(map(lambda x:x**2,nums)))

squares = [-4,-1,0,3,10]
print("squares: "+str(squares))
sorted_squares = sortedSquares(squares)
print("sorted_squares: "+str(sorted_squares))