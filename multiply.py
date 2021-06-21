# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

def multiply(num1, num2):
    total = 0 # final digits
    o = ord('0') # repeating var
    # nested loop
    for i in range(len(num2)):
        t = 0 # sub total
        for j in range(len(num1)):
            t += 10**j * (ord(num1[-j-1]) - o) * (ord(num2[-i-1]) - o)
        total += 10**i * t
    return str(total)
    
