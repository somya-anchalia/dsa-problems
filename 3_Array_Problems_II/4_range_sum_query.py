class NumArray:
    from typing import List
    def __init__(self, nums: List[int]):
        self.sum = []
        sum_till = 0
        for i in nums:
            sum_till += i
            self.sum.append(sum_till)

    def sumRange(self, i: int, j: int) -> int:
        if i > 0 and j > 0:
            return self.sum[j] - self.sum[i - 1]
        else:
            return self.sum[i or j]


# Your NumArray object will be instantiated and called as such:
nums= [-2,0,3,-5,2,-1]
obj = NumArray(nums)
left = 1
right = 3
param_1 = obj.sumRange(left,right)
print(param_1)