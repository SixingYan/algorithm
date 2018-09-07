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
直接的做法就是 先正常生成 所有子集，再做去除重复
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
        out = [[]]
        for n in sorted(nums):
            out += [i+[n] for i in out]
        rst = set([tuple(i) for i in out])
        return list([list(i) for i in rst])
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