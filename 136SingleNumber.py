"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        
        i = 0
        while i < len(nums):
            if i == len(nums)-1:
                value = nums[i]
                break
            if nums[i] != nums[i+1]:
                value = nums[i]
                break
            else:
                i += 2
                
        return value
"""
Fast
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for num in nums:
            res^=num
        return res