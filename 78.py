"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nlen = len(nums)
        if nlen == 0:
            return [[]]
        #nums = sorted(nums) #这里不用sort就行
        result = set([])
        for i in range(2**nlen):
            indxs = self.genIndx(i, nlen)
            result.add(tuple([nums[i] for i in range(nlen) if indxs[i] == '1']))
        return list(result)
    def genIndx(self, n, strlen):
        b2str = str(bin(n))[2:]
        b2len = len(b2str)
        if b2len < strlen:
            b2str = '0' * (strlen-b2len) + b2str
        return list(b2str)
"""
Fast
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        out = [[]]
        
        for n in nums:
            out += [i+[n] for i in out]
        
        return out