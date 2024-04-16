# Question

# Given a string s consisting of words and spaces, return the length
# of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

# ________________________________________________________________________________________________________________________

# Example 1

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# ________________________________________________________________________________________________________________________

# Example 2

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# ________________________________________________________________________________________________________________________

# Example 3

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# ________________________________________________________________________________________________________________________

def lengthOfLastWord(s):
    # "i" is going to be set to the end of the string
    # Take the length -1 takes the index of the last character then set length to 0
    i, length = len(s) -1, 0

    # Eliminate leading white spaces
    while s[i] == " ":
        # We decrement since starting at the end.
        i -= 1
    # Then we count the characters to determine the length.
    # i is going to be at some word need to make sure i is in bound in the string.
    # Then while character at index i is not a space because want length of the word. 
    # If get to space character can exit
    while i >= 0 and s[i] != " ":
        # If character is spotted increment length by 1 and know the length of last word is returned.
        length += 1
        # Decrement the pointer to stop loop
        i -= 1
    return length

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord(" fly me to the moon"))
print(lengthOfLastWord("luffy is still a joyboy"))