# Given two binary strings a and b, return their sum as a binary string.

# Example:
# Input: a = "11", b = "1"
# Output: "100"

def addBinary(a, b):
    carry = 0
    result = ''
    if len(a) < len(b):
        a, b = b, a
    for i in range(1, len(a)+1):
        d1 = int(a[-i])
        d2 = int(b[-i]) if i <= len(b) else 0
        d = d1 + d2 + carry
        if d == 0:
            result = '0' + result
            carry = 0
        elif d == 1:
            result = '1' + result
            carry = 0
        elif d == 2:
            result = '0' + result
            carry = 1
        else:
            result = '1' + result
            carry = 1
    if carry == 1:
        result = '1' + result
    return result
    
