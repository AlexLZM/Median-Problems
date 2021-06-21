#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# O(N*K)

def groupAnagrams(strs):
    anas = collections.defaultdict(list)
    o = ord('a') # save re-use var
    for word in strs:
        l = [0] * 26
        for c in word:
            l[ord[c]-o] += 1
        anas[tuple(l)].append(word)
    return anas.values()
