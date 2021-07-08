# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

def permutationUnique(nums):
    q = collections.deque([[]])
    nums.sort() # sort an break will handle the duplicates
    for num in nums:
        for j in range(len(q)):
            old = q.popleft()
            for i in range(len(old)+1):
                new = old[:] # copy
                new.insert(i, num)
                q.append(new)
                if i < len(old) and old[i] == num:
                    # after inserting num to a position of same value, break to next old permutation in queue
                    # prevents duplicates
                    break
    return q
            
