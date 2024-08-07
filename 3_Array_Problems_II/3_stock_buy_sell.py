from typing import List

def maxProfit(prices: List[int]) -> int:
    buy_price = prices[0]
    profit = 0

    for p in prices[1:]:
        if buy_price > p:
            buy_price = p
        
        profit = max(profit, p - buy_price)
    
    return profit

transactions = [7,1,3,4,5,2]
max_profit = maxProfit(transactions)
print(max_profit)
