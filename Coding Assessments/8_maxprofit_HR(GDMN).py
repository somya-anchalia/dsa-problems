# Cutting Metal Surplus:

# The owner of a construction company has a surplus of rods of arbitrary lengths. A local contractor offers to buy any of the surplus, as long as all the rods have the same exact integer length, referred to as saleLength. The number of sellable rods can be increased by cutting each rod zero or more times, but each cut has a cost denoted by costPerCut. After all cuts have been made, any leftover rods having a length other than saleLength must be discarded for no profit. The owner's total profit for the sale is calculated as:

# totalProfit = (totalUniformRods * saleLength * salePrice) - (totalCuts x*costPerCut)

# where totalUniformRods is the number of sellable rods, salePrice is the per unit length price that the contractor agrees to pay, and totalCuts is the total number of times the rods needed to be cut.

# Example:
# lengths = [30, 59, 110]
# costPerCut = 1
# salePrice = 10 per unit length 

# The following are tests based on lengths that are factors of 30, the length of the shortest bar. Factors of other lengths might also be tested, but this demonstrates the methodology.

# Working through the first stanza, length = 30, it is the same length as the first rod, so no cuts are
# required and there is 1 piece. For the second rod, cut and discard the excess 29 unit rod. No more cuts are necessary and another 1 piece is left to sell. Cut 20 units off the 110 unit rod to discard leaving 90 units, then make two more cuts to have 3 more pieces to sell. Finally sell 5
# totalUniformRods, saleLength = 30 at salePrice = 10 per unit length for 1500. The cost to produce
# was totalCuts = 4 times costPerCut = 1 per cut, or 4. Total revenue = 1500-4=1496. The maximum
# revenue among these tests is obtained at length 5 for 1913.

# Function Description
# Complete the function maxProfit based on details below:

# maxProfit has the following parameters): costPerCut: cost to make a cut salePrice: per unit length sales price lengths[n]: integer rod lengths
# Returns:
# int: maximum possible profit

# Constraints
# 1 ≤ n ≤ 50
# 1 ≤ lengthsli] ≤ 10*
# 1 ≤ salePrice, costPerCut ≤ 1000


def maxProfit(costPerCut, salePrice, lengths):
    def calculate_profit(sale_length):
        total_uniform_rods = 0
        total_cuts = 0
        
        for length in lengths:
            if length < sale_length:
                continue
            
            num_pieces = length // sale_length
            leftover = length % sale_length
            
            total_uniform_rods += num_pieces
            if leftover > 0:
                total_cuts += num_pieces
            else:
                total_cuts += num_pieces - 1
        
        profit = (total_uniform_rods * sale_length * salePrice) - (total_cuts * costPerCut)
        return profit
    
    max_length = max(lengths)
    max_profit = float('-inf')
    
    for sale_length in range(1, max_length + 1):
        profit = calculate_profit(sale_length)
        if profit > max_profit:
            max_profit = profit
    
    return max_profit

# Example usage:
lengths = [30, 59, 110]
# lengths = [26,103,59]
costPerCut = 1
salePrice = 10
print(maxProfit(costPerCut, salePrice, lengths))  # Output should be 1913
