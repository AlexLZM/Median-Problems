# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

# Example:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.

# 2 pointers 
# use ordered dict to track left pointer

def lengthOfLongestSubstringKDistinct(s, k):
    positions = collections.OrderedDict() # remember last occurence of values
    res = 0
    l = 0
    for r, c in enumerate(s):
        positions[c] = r # update last occurence
        positions.move_to_end(c) # put key of c to the last
        if len(positions) > k: # max reached, sub string ends on r - 1
            res = max(res, r - l) 
            _, l = positions.popitem(last=False) # get first value in the ordered dict to determine l
            l += 1
     return max(res, r - l + 1) # final check when r == len(s) - 1
