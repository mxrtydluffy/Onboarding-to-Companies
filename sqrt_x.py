# Question

# Given a non-negative integer x, return the square root of x
# rounded down to the nearest integer. The returned integer should
# be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

#_______________________________________________________________________________________________________________________

# Question #1

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

#_______________________________________________________________________________________________________________________

# Question #2

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

#_______________________________________________________________________________________________________________________

def mySqrt(x):
    # Initilize l & r
    l, r = 0, x
    res = 0

    # Run binary search
    while l <= r:
        m = l + ((r - l) // 2)
        # Run equalities
        if m**2 > x:
            r = m - 1
        # Opposite
        elif m**2 < x:
            l = m + 1
            # mid value could be result
            res = m
        # m**2 does not eqal x
        else:
            return m
    return res

print(mySqrt(4))
print(mySqrt(8))