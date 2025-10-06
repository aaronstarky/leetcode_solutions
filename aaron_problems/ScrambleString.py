def scramble(s):
    """
    Rearranges a string based on character index.

    Characters at indices that are multiples of 4 or have a remainder of 3 when divided by 4 
    are moved to the 'right' part of the string. The remaining characters are placed in the 'left' part,
    which is then reversed. Finally, the reversed 'left' part is concatenated with the 'right' part.

    Args:
        s: The input string.

    Returns:
        The scrambled string.
    """
    right = []
    left = []
    for i in range(len(s)):
        if i % 4 == 0 or i % 4 == 3:
            right.append(s[i])
        else:
            left.append(s[i])
    # Reverse the 'left' list and convert it to a string.
    left = left[::-1]
    ls = "".join(left)
    # Convert the 'right' list to a string.
    rs = "".join(right)
    # Return the concatenated strings.
    return ls + rs

# Example usage of the scramble function
# string_to_scramble = "Hello World"
# scrambled_string = scramble(string_to_scramble)
# print(f"Original string: {string_to_scramble}")
# print(f"Scrambled string: {scrambled_string}")

s1 = 'abcd'
s2 = 'abcdef'
s3 = 'abcdefgh'

print(scramble(s1))
print(scramble(s2))
print(scramble(s3))
