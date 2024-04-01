# Question

# Given a sorted array of distinct integers and a target value,
# return the indez if the target is found. If not, return the
# index where it would be if it were inserted in order.

# You must write an algorithm with 0(log n) runtime complexity

# ______________________________________________________________________________________________________________________________________

# Example 1

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# ______________________________________________________________________________________________________________________________________

# Example 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# ______________________________________________________________________________________________________________________________________

# Example 3

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# ______________________________________________________________________________________________________________________________________

def searchInsert(nums, target):
    # Initialize left and right pointers at 0.
    # Get the length of numbers -1 (right most value)
    l, r = 0, len(nums) - 1

    # While left corner hasn't crossed right corner
    while 1 <= r:
        mid = (1 + r) // 2

        # Check if target is found
        if target == nums[mid]:
            return mid
        
        # Check if too big
        if target > nums[mid]:
            # Shift towards the right for big numbers
            l = mid + 1
        
        # Check if too small
        else:
            # Search towards the left for small numbers
            r = mid - 1
    # If target is never found return left
    return l

print(searchInsert([1,3,5,6], 5))