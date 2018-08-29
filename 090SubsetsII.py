"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
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
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nlen = len(nums)
        if nlen == 0:
            return [[]]
        nums = sorted(nums)
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
    def onenum(self, x, n):
        return [[x]*i for i in range(n+1)]
    
    def subsets(self, a):
        global d
        if len(a)==0:
            return [[]]
        tmp1=self.onenum(a[0],d[a[0]])
        tmp2=self.subsets(a[1:])
        return [i+j for i in tmp1 for j in tmp2]
        
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global d
        if len(nums)==0:
            return [[]]
        d=dict()
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        a=sorted(d.keys())
        return self.subsets(a)