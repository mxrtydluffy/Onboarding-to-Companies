# Question

# Given an integer x, return true if x is a palindrome, and false otherwise.

#_____________________________________________________________________________________________________________________________________

# Example #1

# Input x = 121
# Output: True
# Explanation: 121 reads as 121 from left to right and from right to left

# _____________________________________________________________________________________________________________________________________

# Example #2

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# _____________________________________________________________________________________________________________________________________

# Example #3

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

def isPalindrome(x):
    # If value is less than 0 its a negative and it won't work so return False
    if x < 0: return False

    # Create divider since its 1 
    div = 1
    # Increase divider that is greater than 10 if so multiply by 100 or 1000
    while x >= 10 * div:
        div *= 10
    
    while x:
        # Compare left and right digits
        if x // div != x % 10: return False

        # Take away left and right digit
        x =(x % div) // 10
        div = div / 100
    return True

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))