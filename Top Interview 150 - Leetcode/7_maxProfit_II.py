from typing import List

def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    max_profit = 0
    for i in range(n-1):
        if prices[i+1] > prices[i]:
            max_profit += (prices[i+1] - prices[i])
    return max_profit

if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]

    maxPro = maxProfit(arr)

    print("Max profit is: ", maxPro)

