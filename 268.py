"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()  
        
        if nums[0] != 0:
            value = 0
        
        if nums[len(nums)-1] != len(nums):
            return len(nums)
        
        else:
            for i in range(len(nums)-1):
                if nums[i] + 1 < nums[i+1]:
                    value = nums[i] + 1
                    break
        return value
"""
Fast
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (n*(n+1)/2 ) - sum(nums)