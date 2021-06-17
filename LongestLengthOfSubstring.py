# Given a string s, find the length of the longest substring without repeating characters.

# Example:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def LongestLengthOfSubstring(s):
  streak = {} # dict to save a char's last occurrce index
  l = 0 # left pointer, we will keep non-repetitive invariant in s[l:r]
  res = 0 # final answer
  for r in range(n:=len(s)):
    if s[r] in streak and (prev:=steak[s[r]]) >= l:
      # invariant violated, calculate length
      res = max(res, r - l)
      l = prev + 1
    streak[s[r]] = r # update the last occurence of s[i]

  # final calculation
  res = max(res, n - l)
  return res
