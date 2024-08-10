# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

from typing import List

def maxProfit(prices: List[int]) -> int:
        n = len(prices)
        profit = [0]*n
        global_min = prices[0]
        for i in range(1,n):
            global_min = min(global_min,prices[i])
            profit[i] = max(profit[i-1],prices[i]-global_min)
        
        res = max(profit[-1],0)
        global_max = 0
        for i in range(n-1,0,-1):
            global_max = max(global_max,prices[i])
            res = max(res,profit[i-1]+global_max-prices[i])
        
        return res

transactions = [7,1,3,4,5,2]
max_profit = maxProfit(transactions)
print(max_profit)
