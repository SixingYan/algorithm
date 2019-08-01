"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""
"""
Comments

Fast 用了一些修改原始数组的方法，没看懂
"""
"""
My
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        x, n  = max(nums), min(nums)
        res = 1
        if n > 1:
            return 1
        else:
            i = 1
            while i < x: # 这个地方直接用range的话可能会内存溢出，因为可能会出现超过范围的整数
                if i not in nums:
                    return i
                i += 1
            return max(1, x+1)
"""
Fast
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for v in nums:
            temp = v
            while(temp <= n and temp > 0):
                t1 = nums[temp - 1]
                nums[temp - 1] = temp
                if temp == t1:
                    break
                temp = t1

        for i,v in enumerate(nums):
            if i + 1 != v:
                return i + 1

        return n + 1