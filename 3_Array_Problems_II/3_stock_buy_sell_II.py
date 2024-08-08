# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

from typing import List

def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    max_profit = 0
    for i in range(n-1):
        if prices[i+1] > prices[i]:
            max_profit += (prices[i+1] - prices[i])
    
    return max_profit

transactions = [7,1,3,4,5,2]
max_profit = maxProfit(transactions)
print(max_profit)
