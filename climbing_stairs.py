# Question

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#_______________________________________________________________________________________________________________________

# Example 1

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

def climbStairs(n: int) -> int:
    # Each step 
    one, two = 1, 1

    # Continuously update variables one & two using a for loop
    for i in range(n -1):
        # store one in a temporary variable before its updated
        temp = one
        # Adding two previous values and getting new result.
        one = one + two
        # set to temp variable instead of one + two
        two = temp

    # return one since its whats being calculated
    return one

print(climbStairs(2))
print(climbStairs(3))