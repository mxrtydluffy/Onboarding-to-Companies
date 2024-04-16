# Question

# You are given a large integer represented as an integer array
# digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant
# in left-to-right order. The large integer does not contain any
# leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# ________________________________________________________________________________________________________________________

# Example 1

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# ________________________________________________________________________________________________________________________

# Example 2

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# ________________________________________________________________________________________________________________________

# Example 3

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

# ________________________________________________________________________________________________________________________

def plusOne(digits):
    # Reverse integer 
    digits = digits[::-1]
    # Carry one if needed. i will represent index currently at
    # Initialize single value 1 because need a 1 at the digit. Then 0 at the digits array
    one, i = 1, 0

    # While digit is equal to one
    while one:
        # Need to check if i will go out of bounds.
        # If i is still in bounds then increment
        if i < len(digits):
            # Need to reconsider if i == 9 then need to carry
            if digits[i] == 9:
                # if add one to this i will reset back to 0
                digits[i] = 0
            # If the digit is not 9 then increment it by 1.
            else:
                digits[i] += 1
                # Since if its not 9 won't have a carry anymore we change "one" to 0 since not adding anything
                one = 0
        # Go out of bounds.
        # Reached the end no more digits to add but have a 1 value.
        else:
            # Would take digits and append 1 since adding a new digit into the array
            digits.append(1)
            # No we have no more carry, reset one back to 0
            one = 0
        # increment index regardless which if condition executes since doing a while loop
        i += 1
    # Return digits but since initially reserved it at the beginning, undo the reverse.
    # Reserve it again to have it in the correct format
    return digits[::-1]

print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))