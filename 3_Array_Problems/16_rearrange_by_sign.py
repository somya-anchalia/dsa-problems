from typing import List

def RearrangebySign(A: List[int]) -> List[int]:
    n = len(A)
    
    # Define array for storing the ans separately.
    ans = [0] * n
    
    # positive elements start from 0 and negative from 1.
    posIndex, negIndex = 0, 1
    for i in range(n):
        
        # Fill negative elements in odd indices and inc by 2.
        if A[i] < 0:
            ans[negIndex] = A[i]
            negIndex += 2
        
        # Fill positive elements in even indices and inc by 2.
        else:
            ans[posIndex] = A[i]
            posIndex += 2
    
    return ans
    
# Test the function
A = [1,2,-4,-5,4,3,-2,-6]
ans = RearrangebySign(A)
print(ans)