# Question

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

#_______________________________________________________________________________________________________________________

# Example 1

# Input: s = "()"
# Output: true

# Example 2

# Input: s = "()"
# Output: true

# Example 3

# Input: s = "(]"
# Output: false

def isValid(s):
    # To start off create a pair of opening and closing parrenthesis inside a dictionary because need to access
    # the characters later and assign it to a variable.
    opcl = dict(('()', '[]', '{}'))
    # Create list data structure and assign it to a variable.
    stack = []
    # Loop through each charater in the input string
    for idx in s:
        # If the open parentheses are present in the index, append it to stack...
        if idx in '([{':
            stack.append(idx)
        # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not.
        # If not, we need to return false...
        elif len(stack) == 0 or idx != opcl[stack.pop()]:
            return False
    # lastly, we check if the stack is empty or not...
    # If the stack is empty, it means every opened parenthesis is being closed and we can return true, otherwise we return false.
    return len(stack) == 0

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))