# https://leetcode.com/problems/climbing-stairs/description/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
    if n<=2:
        return n

    step_1= 1
    step_2= 2
    ways= 0
    for i in range(2,n):
        ways=step_1+step_2
        step_1=step_2
        step_2=ways

    return ways

ways = climbStairs(4)
print(ways)
