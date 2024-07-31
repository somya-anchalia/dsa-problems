# https://leetcode.com/problems/minimum-cost-for-tickets/description/
from typing import List
from collections import defaultdict

def mincostTickets(days: List[int], costs: List[int]) -> int:
        dp = defaultdict(lambda: 0)
        print(dp)
        for d in range(1, days[-1] + 1):
            dp[d] = (
                min(
                    dp[d - 1] + costs[0],
                    dp[d - 7] + costs[1],
                    dp[d - 30] + costs[2],
                )
                if d in days
                else dp[d - 1]
            )
            print(dp)
        return dp[days[-1]]

days = [1,4,6,7,8,20]
cost = [2,7,15]
min_cost = mincostTickets(days,cost)
print(min_cost)