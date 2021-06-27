# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example:

# Input: nums = [1,1,1], k = 2
# Output: 2


# use counter to remember the occurence of sum of first i items
# a sum range [i, j) is range [0, j) - range [0, i), we hope it to be k
# check if key (range [0, j) - k) in the counter and add its value to result count

def subarraySum(nums, k):
    s = 0
    count = 0
    sum_counter = {0:1} # sum from 0 to 0 is 0
    for i, num in enumerate(nums, 1):
        s += num
        if s - k in sum_counter:
            count += sum_counter[s - k]
        if s in sum_counter:
            sum_counter[s] += 1
        else:
            sum_counter[s] = 1
    return count
