"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        n = len(nums)
        tmp = [0] * n

        def next_num(a, ni):
            if ni == n:
                result.append(copy.copy(tmp))
                return
            for lj in range(len(a)):
                tmp[ni] = a[lj]
                b = a[:]
                b.pop(lj)
                next_num(b, ni+1)

        a = nums[:]
        next_num(a, 0)
        return result
        
"""
Fast
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(i):
            if i == len(nums) - 1:
                res.append(list(nums))
                return
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                helper(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        res = []
        helper(0)
        return res