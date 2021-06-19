# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

# Example:
# Input: nums = [1,2,3]
# Output: [1,3,2]

def nextPermutation(nums):
    '''
    We found the pattern to find the next permutation:
    1. from right to left, find the first index 'i' where value is greater than its left
    2. reverse the part nums[i:]
    3. find the next greater value of nums[i - 1] after i (from the right) and exchange the values with nums[i - 1]
        (cound be done by binary search as the part is monotonicly increasing)
    
    if at 1. we fail to find i, reverse the whole nums
    
    Time complexity: order n to find i, order n to reverse, order log(n) to find next greater value
    O(n)
    '''
    for i in range(len(nums)-1, 0, -1):
        if nums[i] > nums[i-1]:
            nums[i:] = nums[i:][::-1]
            
            j = bisect.bisect_right(nums, nums[i-1], i) # leftbound is i
            nums[i-1], nums[j] = nums[j], nums[i-1]
    nums.reverse()
            
