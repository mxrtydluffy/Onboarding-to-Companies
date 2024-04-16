# Question

# Given two binary strings a and b, return their sum as a
# binary string.

#_______________________________________________________________________________________________________________________

# Question #1

# Input: a = "11", b = "1"
# Output: "100"

#_______________________________________________________________________________________________________________________

# Question #2

# Input: a = "1010", b = "1011"
# Output: "10101"

#_______________________________________________________________________________________________________________________

def addBinary(a, b):
    # Returning result in string form
    res = ""
    carry = 0

    # Since starting at the right most end when adding, reverse input strings.
    a, b = a[::-1], b[::-1]

    # Since not the same size reiterate in the string to see the max value
    for i in range(max(len(a), len(b))):
        # Add digit by digit
        # Can reach the end of one string than the other.
        # If not in bounds give default value of 0
        # ord() is converting character to integer
        digitA = ord(a[i]) if i < len(a) else 0
        digitB = ord(b[i]) if i < len(b) else 0

        # Sum into total
        total = digitA + digitB + carry
        char = str(total % 2)
        # Take result character and add to result string.
        res = char + res
        # Update carry int
        carry = total // 2
    # Carry can be eqaul to 0 but can be equal to 1
    if carry:
        res = "1" + res
    return res

print(addBinary("11", "1"))
print(addBinary("1010", "1011"))