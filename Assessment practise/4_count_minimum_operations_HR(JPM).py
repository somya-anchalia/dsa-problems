# A shop in HackerLand contains n items where the price of the i^th item is price[i]. In one operation, the price of any one item can be increased or decreased by 1.
# Given q queries denoted by the array query[], find the minimum number of operations required to make the price of all items equal to each query[i] (0 ≤ i < q).
# Note: All queries are independent of each other, i.e., the original price of items is restored after the completion of each query.
# Example:
# Consider n = 3, q = 4, price[] = [1, 2, 3], query[] = [3, 2, 1, 5]

# query[0] = 3. The number of operations required = [2, 1, 0] to make the price of all
# elements equal to 3. Total number of operations = 2 + 1 + 0 = 3.
# query[1] = 2, operations required = [1, 0, 1], 1 + 0 + 1 = 2
# query[2] = 1, operations required = [0, 1, 2], 0 + 1 + 2 = 3
# query[3] = 5, operations required = [4, 3, 2], 4 + 3 + 2 = 9
# The answer is [3, 2, 3, 9]
# Function Description:
# Complete the function countMinimumOperations has the following parameters:
# int price[n]: the original prices of each item int query[q]: the queries
# Returns
# long_int[q]: the answers to the queries in their order of input


# Solution method 1:
def countMinimumOperations(price, query):
    results = []
    for q in query:
        total_operations = sum(abs(p - q) for p in price)
        results.append(total_operations)
    return results


# Solution method 2:
from bisect import bisect_left
def countMinimumOperations(price, query):
    price.sort()
    n = len(price)
    
    # Compute prefix sums
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + price[i]
    
    results = []
    
    for q in query:
        # Find the index where q would be inserted to keep price sorted
        pos = bisect_left(price, q)
        
        # Operations to make all prices to the left of pos equal to q
        left_ops = q * pos - prefix_sum[pos]
        
        # Operations to make all prices to the right of pos equal to q
        right_ops = (prefix_sum[n] - prefix_sum[pos]) - q * (n - pos)
        
        results.append(left_ops + right_ops)
    
    return results

# Example usage:
price = [1, 2, 3]
query = [3, 2, 1, 5]
result = countMinimumOperations(price, query)
print(result)  # Output: [3, 2, 3, 9]
