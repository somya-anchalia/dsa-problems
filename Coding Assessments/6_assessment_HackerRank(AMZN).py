# As an aspiring developer at Amazon, you are building a prototype for a cart management service
# There is an array of integers, items, that represents the item ids present in the cart initially.
# Given an array of q integers, query, your service must perform as follows. Each integer is an item id to be added to or removed from the cart.
# • If the query integer is positive, add the integer representing an item id to the back of the cart.
# • If the integer is negative, remove the first occurrence of the integer from the cart

# Report an array that represents the final cart after processing all the queries. It is guaranteed that the final cart is non-empty and the integers in the integer in the queries are not equal to 0.

# Example
# For example. initially, there are n = 5 items in the cart represented as cart = [1, 2, 1, 2, 1] and queries = [-1, -1, 3, 4, -3].

# Report [2, 2, 1, 4] as the final cart.

# Function Description
# Complete the function processQueriesOnCart in the editor below.

# processQueriesOnCart has the following parameters:
# int items[n]: items initially in the cart
# int query[q]: items to add or remove

def processQueriesOnCart(items, query):
    cart = items[:]

    for q in query:
        if q > 0:
            cart.append(q)
        else:
            if -q in cart:
                cart.remove(-q)

    return cart

# Example usage
items = [1, 2, 1, 2, 1]
query = [-1, -1, 3, 4, -3]
print(processQueriesOnCart(items, query))  # Output: [2, 2, 1, 4]

items = [5, 6, 7]
query = [8, -6, 5, -7]
print(processQueriesOnCart(items, query))  # Output: [5, 8, 5]
