
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n = len(s)
        if n <= 2:
            return True
        if n == 3:
            return len(set(s)) < 3

        # n > 3
        # divide s into 3 parts: left, mid, right
        div = n//3 
        left = s[:div]
        right = s[n-div:]

        # size of left and right are div

        # case: deletion in mid or no deletion
        if (ends := (left+right)) == ends[::-1]:
            return self.validPalindrome(s[div:n-div])

        # case: deletion in left
        # right size = div - 1 (to have same size of left)
        if (seq := s[div:n-div+1]) == seq[::-1]:
            return self.validPalindrome(left + right[1:])

        # case: deletion in right
        # left size = div - 1 (to have same size of right)
        if (seq := s[div-1:n-div]) == seq[::-1]:
            return self.validPalindrome(left[:-1] + right)

        return False
    # 28ms (100%)
